from pydantic import BaseModel

class HotelResponse(BaseModel):
    name: str
    stadium_name: str
    city: str
    price: float
    rating: float
    distance_km: float
    score: float
