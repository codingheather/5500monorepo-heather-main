from typing import Union

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    category: str


@app.get("/api") # client sends get() request
def first_api(): # app returns the client a response with this piece of info
    return {"msg": "hello_worldXXXXX"} 


@app.get("/books/{path_param}") # with path parameters
def first_apiV2(path_param: str):
    return {"msg": path_param}


@app.get("/books/") # with query parameters
def first_apiV3(title: str):
    return {"msg": title}


@app.get("/books/category/{category}") # with path parameters AND query parameters
def first_apiV4(category: str, author: str):
    return {"category": category, "author": author}


@app.post("/books/create_book") # use the data from the caller to create sth in the backend
def first_apiV5(new_book=Body()):
    print(new_book)
    return {"msg": new_book}


@app.put("/books/{old_title}") # To update data
def first_apiV6(new_book: Book, old_title: str):
    return {'old_title': old_title, 'title': new_book.title, 'author': new_book.author, 'category': new_book.category}


@app.delete("/books/{title}")
def first_apiV7(title: str):
    return {"msg": title}