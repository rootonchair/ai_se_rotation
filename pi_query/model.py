from pydantic import BaseModel

class Order(BaseModel):
    precision: int
