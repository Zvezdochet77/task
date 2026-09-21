from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import datetime
from typing import List 

class UserRead (BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: int
    model_config = ConfigDict(from_attributes=True) 

class OrderStatusRead (BaseModel):
    id: int
    code: int
    title: str
    model_config = ConfigDict(from_attributes=True) 

class OrderItemRead (BaseModel):
    product_id: int
    title: str
    price: float
    quantity: int 
    total: float
    
class OrderDetailResponse (BaseModel):
    id: int
    user: UserRead
    staus: OrderStatusRead
    items: list [OrderItemRead]
    total: float

class OrderItemCreate (BaseModel):
    product_id: int
    quantity: int = Field (gt=0)
    
class OrderCreate (BaseModel):
    user_id: int
    items: list [OrderItemCreate]

class OrderStatusUpdate (BaseModel):
    status_id: id
    




    








    