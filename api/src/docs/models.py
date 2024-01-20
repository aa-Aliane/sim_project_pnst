from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database import Base
import uuid




# These table
class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    doc_id = Column(String)
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
    authors = Column(String)


