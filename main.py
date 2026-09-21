from database import Base, engine, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from models import Order, OrderStatus, Product, User, order_items
from schemas import (
    OrderDetailResponse, 
    OrderItemRead,
    OrderCreate,
    OrderStatusUpdate
)
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from typing import List 

app = FastAPI(title="Order API Practice")

@app.get (
    "/api/v1/orders/{order_id}",
    response_model= OrderDetailResponse
)
def get_order_detail(order_id: int, db: Session = Depends(get_db)):
    order = (
        db.query(Order)
        .options(joinedload(Order.user), joinedload(Order.status))
        .filter (Order.id == order_id)
        .first () 
    )
    if not order:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    raw_items = db.execute (
        select (
            Product.id.label("product_id"),
            Product.title,
            Product.price,
            order_items.c.quantity,    
        )
        .join(order_items, Product.id == order_items.c.product_id)
        .where (order_items.c.order_id == order.id)
    ).fetchall()