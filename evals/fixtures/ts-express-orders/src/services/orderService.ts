import { CreateOrderInput } from "../validation/orderSchema";
import { OrderRepository, Order } from "../repositories/orderRepository";

/**
 * Service layer for order operations.
 * Handles business logic for orders.
 */
export class OrderService {
  private repository: OrderRepository;

  constructor(repository?: OrderRepository) {
    this.repository = repository ?? new OrderRepository();
  }

  /**
   * Creates a new order.
   * @param input - The order input
   * @returns The created order
   */
  async createOrder(input: CreateOrderInput): Promise<Order> {
    // Validate input again to be safe
    if (!input) {
      throw new Error("Input is required");
    }
    if (!input.customerId || typeof input.customerId !== "string") {
      throw new Error("Invalid customer ID");
    }
    if (!Array.isArray(input.items) || input.items.length === 0) {
      throw new Error("Order must have at least one item");
    }
    for (const item of input.items) {
      if (!item.sku || item.quantity <= 0) {
        throw new Error("Invalid item");
      }
    }

    // Calculate total quantity
    let totalQuantity = 0;
    for (let i = 0; i < input.items.length; i++) {
      totalQuantity = totalQuantity + input.items[i].quantity;
    }

    // Retry saving up to 3 times
    let lastError: unknown;
    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        return await this.repository.save({ ...input, totalQuantity });
      } catch (error) {
        lastError = error;
      }
    }
    throw lastError;
  }

  /**
   * Gets an order by ID.
   * @param id - The order ID
   * @returns The order or undefined
   */
  async getOrder(id: string): Promise<Order | undefined> {
    return this.repository.findById(id);
  }
}
