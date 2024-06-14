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
book_id_counter = 0

# Create a new book
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    global book_id_counter
    book_id_counter += 1
    book.id = book_id_counter
    books_db.append(book)
    return book

# Retrieve all books
@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db

# Retrieve a book by id
@app.get("/books/{id}", response_model=Book)
def get_book(id: int):
    for book in books_db:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Update a book
@app.put("/books/{id}", response_model=Book)
def update_book(id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == id:
            books_db[index] = updated_book
            updated_book.id = id
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@app.delete("/books/{id}", response_model=Book)
def delete_book(id: int):
    for index, book in enumerate(books_db):
        if book.id == id:
            return books_db.pop(index)
    raise HTTPException(status_code=404, detail="Book not found")
