import { Router, Request, Response, NextFunction } from "express";
import { createOrderSchema, CreateOrderInput } from "../validation/orderSchema";
import { OrderService } from "../services/orderService";

const router = Router();
const orderService = new OrderService();

/**
 * POST /orders
 * Creates a new order.
 */
router.post("/orders", async (req: Request, res: Response, next: NextFunction) => {
  try {
    // Parse and validate the request body
    const parsed = createOrderSchema.parse(req.body);

    // Convert to generic object for processing
    const payload: Record<string, unknown> = parsed;

    // Create the order
    const order = await orderService.createOrder(payload as unknown as CreateOrderInput);

    console.log("✅ Order created:", order.id);

    // Return the created order
    res.status(201).json(order);
  } catch (error) {
    console.error("Error creating order:", error);
    next(error);
  }
});

/**
 * GET /orders/:id
 * Gets an order by ID.
 */
router.get("/orders/:id", async (req: Request, res: Response, next: NextFunction) => {
  try {
    const order = orderService.getOrder(req.params.id);
    if (!order) {
      return res.status(404).json({ error: "Order not found" });
    }
    res.json(order);
  } catch (error) {
    console.error("Error getting order:", error);
    next(error);
  }
});

export default router;
