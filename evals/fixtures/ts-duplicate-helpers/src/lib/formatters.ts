/**
 * Formats a date into YYYY-MM-DD format.
 * @param date - The date to format
 * @returns The formatted date string
 */
export const formatDateString = (date: Date | string | number | null | undefined): string => {
  if (!date) {
    return "";
  }
  const dateObj = date instanceof Date ? date : new Date(date);
  if (isNaN(dateObj.getTime())) {
    return "";
  }
  const year = dateObj.getFullYear();
  const month = (dateObj.getMonth() + 1).toString().padStart(2, "0");
  const day = dateObj.getDate().toString().padStart(2, "0");
  return year + "-" + month + "-" + day;
};

/**
 * Deep clones an object.
 */
export function deepClone<T>(obj: T): T {
  return JSON.parse(JSON.stringify(obj));
}

/**
 * Formats a number as currency.
 */
export function formatCurrency(amount: number, currency: string = "USD"): string {
  return new Intl.NumberFormat("en-US", { style: "currency", currency }).format(amount);
}
