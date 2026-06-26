from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    rating: float
    restaurant: str
    image_url: str
    is_veg: bool