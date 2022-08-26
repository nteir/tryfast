import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import Book as BookSchema
from models import Book as BookModel
from schemas import Author as AuthorSchema
from models import Author as AuthorModel

load_dotenv('.env')
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/book/')
def get_books():
    books = db.session.query(BookModel).all()
    return books

@app.post('/book/', response_model=BookSchema)
def add_book(book: BookSchema):
    db_book = BookModel(
        title=book.title,
        language=book.language,
        rating=book.rating,
        author_id=book.author_id
    )
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.post('/author/', response_model=AuthorSchema)
def add_author(author: AuthorSchema):
    db_author = AuthorModel(
        name=author.name
    )
    db.session.add(db_author)
    db.session.commit()
    return db_author
