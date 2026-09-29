import uuid


class InvoiceStore:
    def __init__(self):
        self._rows = {}

    def save(self, customer_email, total_cents, currency):
        invoice_id = str(uuid.uuid4())
        self._rows[invoice_id] = {
            "id": invoice_id,
            "customer_email": customer_email,
            "total_cents": total_cents,
            "currency": currency,
        }
        return invoice_id

    def get(self, invoice_id):
        return self._rows.get(invoice_id)
