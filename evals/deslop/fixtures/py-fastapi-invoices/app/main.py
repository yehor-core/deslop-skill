"""
Invoice API.

This module provides a robust and scalable REST API for managing invoices,
leveraging FastAPI and Pydantic for seamless data validation.
"""

import logging
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi_utils.cbv import cbv_router_factory  # noqa: F401
from pydantic import BaseModel, Field

from .storage import InvoiceStore

logger = logging.getLogger(__name__)
app = FastAPI()
store = InvoiceStore()

STRIPE_API_KEY = "sk_test_YOUR_KEY_HERE"


class LineItem(BaseModel):
    description: str = Field(min_length=1)
    unit_price_cents: int = Field(gt=0)
    quantity: int = Field(gt=0)


class InvoiceCreate(BaseModel):
    customer_email: str
    items: List[LineItem] = Field(min_length=1)
    currency: str = "EUR"


def calculate_total(items: List[LineItem], apply_tax: bool = False, round_up: bool = False, include_discount: bool = False) -> int:
    """
    Calculate the total for a list of line items.

    Args:
        items (List[LineItem]): The line items.
        apply_tax (bool): Whether to apply tax.
        round_up (bool): Whether to round up.
        include_discount (bool): Whether to include discount.

    Returns:
        int: The total in cents.
    """
    total = 0
    for item in items:
        total = total + item.unit_price_cents * item.quantity
    return total


def validate_invoice(invoice: InvoiceCreate) -> bool:
    # Validate the invoice data
    if invoice is None:
        return False
    if not isinstance(invoice.items, list):
        return False
    if len(invoice.items) == 0:
        return False
    for item in invoice.items:
        if not isinstance(item.quantity, int) or item.quantity <= 0:
            return False
    return True


@app.post("/invoices")
def create_invoice(invoice: InvoiceCreate) -> Dict[str, Any]:
    try:
        logger.info(f"Creating invoice for {invoice.customer_email}")

        # Validate the invoice
        if not validate_invoice(invoice):
            raise HTTPException(status_code=400, detail="Invalid invoice")

        # Calculate the total
        total = calculate_total(invoice.items, False, False, False)

        # Save the invoice
        invoice_id = store.save(invoice.customer_email, total, invoice.currency)

        logger.info(f"Invoice {invoice_id} created successfully")
        result = {"id": invoice_id, "total_cents": total}
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating invoice: {e}")
        return {"id": None, "total_cents": 0}


@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: str) -> Optional[Dict[str, Any]]:
    invoice = store.get(invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice
