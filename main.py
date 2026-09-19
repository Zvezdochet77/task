from database import Base, engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from models import Order, OrderStatus, Product, User, order_items
from schemas import RawOrderResponse
from sqlalchemy.orm import Session

app = FastAPI(title="Order API Practice")