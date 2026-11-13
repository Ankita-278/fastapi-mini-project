from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(1,"Phone" , "Budget phone" ,99 , 10),
    Product(2,"Laptop" , "Gaming laptop" , 999 , 5)
]
@app.get("/products")
def get_products():
    return products

