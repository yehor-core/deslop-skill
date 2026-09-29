import { createHmac, timingSafeEqual } from "node:crypto";
import type { Request, Response } from "express";
import { enqueue } from "./queue";

const SECRET = process.env.WEBHOOK_SECRET;
if (!SECRET) throw new Error("WEBHOOK_SECRET is not set");

// Provider signs the raw body, not the parsed JSON, so this route must be
// mounted with express.raw(). Re-serializing would change whitespace and
// break the signature.
function signatureMatches(raw: Buffer, header: string | undefined): boolean {
  if (!header) return false;
  const expected = createHmac("sha256", SECRET!).update(raw).digest("hex");
  const given = Buffer.from(header, "hex");
  const want = Buffer.from(expected, "hex");
  return given.length === want.length && timingSafeEqual(given, want);
}

export async function handleWebhook(req: Request, res: Response) {
  if (!signatureMatches(req.body, req.header("x-signature"))) {
    return res.status(401).end();
  }

  let event: { id: string; type: string };
  try {
    event = JSON.parse(req.body.toString("utf8"));
  } catch {
    return res.status(400).send("body is not JSON");
  }

  // Ack fast; the provider retries anything slower than 5s.
  await enqueue(event.id, event.type, req.body);
  res.status(204).end();
}
