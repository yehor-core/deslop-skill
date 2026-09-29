from dataclasses import dataclass


@dataclass(frozen=True)
class Cart:
    subtotal_cents: int
    loyalty_years: int
    coupon: str | None = None


def discount_cents(cart: Cart) -> int:
    percent = min(cart.loyalty_years, 5) * 2
    if cart.coupon == "WELCOME10":
        percent += 10
    return cart.subtotal_cents * percent // 100
