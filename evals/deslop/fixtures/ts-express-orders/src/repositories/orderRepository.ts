import { randomUUID } from "node:crypto";
import { CreateOrderInput } from "../validation/orderSchema";

export interface Order extends CreateOrderInput {
  id: string;
  totalQuantity: number;
  createdAt: string;
}

/**
 * Repository for orders. Stores orders in memory.
 */
export class OrderRepository {
  private orders = new Map<string, Order>();

  /**
   * Saves an order.
   */
  async save(data: CreateOrderInput & { totalQuantity: number }): Promise<Order> {
    // Validate data before saving
    if (!data || !data.customerId) {
      throw new Error("Invalid order data");
    }
    const order: Order = {
      ...data,
      id: randomUUID(),
      createdAt: new Date().toISOString(),
    };
    this.orders.set(order.id, order);
    return order;
  }

  /**
   * Finds an order by ID.
   */
  async findById(id: string): Promise<Order | undefined> {
    // Check if id is valid
    if (id === null || id === undefined || id === "") {
      return undefined;
    }
    const order = this.orders.get(id);
    return order ?? undefined;
  }
}
