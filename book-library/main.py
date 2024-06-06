from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# In-memory database
books_db = []
book_id_counter = 1

# Create a new book
@app.post("/books/")
def create_book(book: Book):
    global book_id_counter
    book.id = book_id_counter
    books_db[id] = {"id": book.id, "Title": book.title, "author": book.author, "year": book.year}
    books_db.append(book)
    book_id_counter += 1
    return {"id": book.id, "Info": books_db[book.id] }

# Retrieve all books
@app.get("/books/", )
def get_books():
    return {"Books": books_db}

# Retrieve a book by id
@app.get("/books/{id}")
def get_book(id: int):
   return books_db[id]

# Update a book
@app.put("/books/{id}")
def update_book(id: int, updated_book: Book):
    books_db[id]["author"] = updated_book.author
    books_db[id]["title"] = updated_book.title
    books_db[id]["year"] = updated_book.year
    return {"id": updated_book.id, "Info": books_db[updated_book.id] }
    

# Delete a book
@app.delete("/books/{id}", response_model=Book)
def delete_book(id: int):
    books_db.pop[id]
    return books_db
