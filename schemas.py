from pydantic import BaseModel


class Book(BaseModel):
    title: str
    language: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    name: str

    class Config:
        orm_mode = True
