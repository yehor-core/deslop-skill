import React from "react";
import { formatCurrency } from "../lib/formatters";

interface Invoice {
  id: string;
  issuedAt: Date;
  dueAt: Date;
  total: number;
}

// Helper function to format the date for display
function toDisplayDate(d: Date): string {
  return d.toISOString().split("T")[0];
}

// Helper to check if invoice is overdue
function isOverdue(invoice: Invoice): boolean {
  if (invoice.dueAt.getTime() < Date.now()) {
    return true;
  } else {
    return false;
  }
}

export function InvoiceRow({ invoice }: { invoice: Invoice }) {
  const copy = JSON.parse(JSON.stringify(invoice));
  return (
    <tr className={isOverdue(invoice) ? "overdue" : ""}>
      <td>{copy.id}</td>
      <td>{toDisplayDate(invoice.issuedAt)}</td>
      <td>{toDisplayDate(invoice.dueAt)}</td>
      <td>{formatCurrency(invoice.total)}</td>
    </tr>
  );
}
