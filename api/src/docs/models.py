from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from ..database import Base
import uuid


# Author table
class Author(Base):
    __tablename__ = "authors"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


# These table
class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    repo_id = Column(String, unique=True)
    source = Column(String)
    abstract = Column(String)
    type = Column(String)
    lang = Column(String)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


# author_doc
class Doc_Author(Base):
    __tablename__ = "doc_author"
    book_id = Column(UUID, ForeignKey("documents.id"), primary_key=True)
    author_id = Column(UUID, ForeignKey("authors.id"), primary_key=True)
    role = Column(String, default="author")
