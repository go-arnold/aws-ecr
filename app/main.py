import os

from fastapi import FastAPI, HTTPException

from app import store
from app.models import Rental, RentalCreate

app = FastAPI(title="Renting App")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "preferred_name": os.getenv("PREFERRED_NAME", "arnold renting"),
    }


@app.get("/rentals", response_model=list[Rental])
def get_rentals():
    return store.list_rentals()


@app.get("/rentals/{rental_id}", response_model=Rental)
def get_rental(rental_id: int):
    rental = store.get_rental(rental_id)
    if rental is None:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental


@app.post("/rentals", response_model=Rental, status_code=201)
def create_rental(payload: RentalCreate):
    rental = Rental(id=store.next_id(), **payload.model_dump())
    return store.add_rental(rental)
