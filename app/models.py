from pydantic import BaseModel


class Rental(BaseModel):
    id: int
    name: str
    description: str
    price_per_day: float
    available: bool


class RentalCreate(BaseModel):
    name: str
    description: str
    price_per_day: float
    available: bool = True
