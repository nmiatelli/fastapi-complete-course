from typing import Optional
from fastapi import  FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):

    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description:str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config={
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author": "Author's name",
                "description": "What the book is about",
                "rating": 5,
                "published_date": 2029
            }
        }
    }



BOOKS = [
    Book( 1,"Clean Code","Robert C. Martin", "A guide to writing clean, maintainable code.", 5, 2012),
    Book( 2, "The Pragmatic Programmer", "Andrew Hunt", "Best practices and philosophy for modern software development.", 5, 2016),
    Book(3,"Atomic Habits","James Clear","How small habits can lead to remarkable results.", 4, 2021),
    Book( 4,"Deep Work","Cal Newport","Focus strategies for productivity in a distracted world.", 4, 2012),
    Book (5,"Python Crash Course","Eric Matthes","A fast-paced introduction to Python programming.",5, 2010),
    Book (6,"Designing Data-Intensive Applications","Martin Kleppman","Martin Kleppmann helps you navigate this diverse landscape by examining the pros and cons of various technologies for processing and storing data",5, 2021)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code= 404, detail="Item not found")
        
        
@app.get("/books/",status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_by_date=[]
    for book in BOOKS:
        if book.published_date == published_date:
            books_by_date.append(book)

    return books_by_date
    

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump()) #converting the request to Book object
    print(type(new_book))
    BOOKS.append(find_book_id(new_book)) 

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1   
    
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    return book

@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
       if BOOKS[i].id == book.id:
           BOOKS[i] = book # type: ignore
           book_changed=True
    if not book_changed:
        raise HTTPException(status_code= 404, detail="Item not found")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range (len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed=True
            break
    if not book_changed:
        raise HTTPException(status_code= 404, detail="Item not found")        
        
