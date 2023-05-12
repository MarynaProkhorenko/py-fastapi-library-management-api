from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base


class DBAuthor(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String(511), nullable=False)
    books = relationship(
        "DBBook",
        back_populates="author",
        cascade="all, delete-orphan"
    )


class DBBook(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(63), nullable=False, unique=True)
    summary = Column(String(511), nullable=True)
    publication_date = Column(Date())
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship(DBAuthor)