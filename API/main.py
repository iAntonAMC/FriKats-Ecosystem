import sqlite3
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import HTTPException 
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import API.models.customers as customers


# Pydantic Base Models:
class Message(BaseModel):
    message:str

class Customer(BaseModel):
    id_customer: int
    customer_name: str

class Category(BaseModel):
    id_category: int
    category_name: str
    common_animes: str

class Product(BaseModel):
    id_product: int
    product_sku: str
    product_name: str
    product_description: str
    product_price: float
    product_image: str
    product_stock: int
    id_category: int

class Sale(BaseModel):
    id_sale: int
    sale_date: str
    id_customer: int
    sale_total: int

class SaleDetail(BaseModel):
    id_detail: int
    id_sale: int
    id_product: int
    total_products: int
    subtotal_price: int


description = """
# API REST for the Anime Store Project [FriKats]
## Description
This project is ment to be a tool for the management of an anime store, it will be able to manage the products, sales, customers and categories of the store.
"""
# Create the FastAPI instance
app = FastAPI(
    title = "FriKats API",
    description = description,
    version = "0.0",
    terms_of_service = "http://example.com/terms/",
    contact = {
        "name": "iAntonAMC",
        "url":"http://github.com/iAntonAMC",
        "email":"1721110125@utectulancingo.edu.mx",
    },
    license_info = {
        "name":"Apache 2.0",
        "url":"https://www.apache.org/licenses/LICENSE-2.0.html",
    })


# CORS
origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


# ROOT
@app.get(
    "/",
    response_model = Message,
    status_code = status.HTTP_202_ACCEPTED,
    summary = "Confirm Connection",
    description = """
    Returns a JSON message to confirm the connection to the API
    parameters: None
    response: JSON message
    errors: 404 - Not Found
    """,
)
async def root():
    response = {"message":"API's connection confirmed"}
    return response

