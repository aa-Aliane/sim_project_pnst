from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base
import uuid

# author_doc
doc_authors = (
    Table(
        "doc_authors",
        Base.metadata,
        Column("document_id", UUID, ForeignKey("documents.id"), primary_key=True),
        Column("author_id", UUID, ForeignKey("authors.id"), primary_key=True),
    ),
)



# Author table
class Author(Base):
    __tablename__ = "authors"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    documents = relationship(
        "Document", secondary="doc_authors", back_populates="authors"
    )


# These table
class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    repo_id = Column(String, unique=True)
    source = Column(String)
    abstract = Column(String)
    type = Column(String)
    lang = Column(String)
    url = Column(String)
    domain = Column(String)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    authors = relationship(
        "Author", secondary="doc_authors", back_populates="documents"
    )


