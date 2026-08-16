from app.models import Rental

_rentals: list[Rental] = [
    Rental(
        id=1,
        name="Cozy Studio Downtown",
        description="A compact studio near the city center.",
        price_per_day=45.0,
        available=True,
    ),
    Rental(
        id=2,
        name="Lakeside Cabin",
        description="A quiet cabin with a lake view.",
        price_per_day=120.0,
        available=False,
    ),
]


def list_rentals() -> list[Rental]:
    return _rentals


def get_rental(rental_id: int) -> Rental | None:
    return next((r for r in _rentals if r.id == rental_id), None)


def next_id() -> int:
    return max((r.id for r in _rentals), default=0) + 1


def add_rental(rental: Rental) -> Rental:
    _rentals.append(rental)
    return rental
