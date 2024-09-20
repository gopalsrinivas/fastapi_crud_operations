from sqlalchemy import Column, String, Text, DateTime, Boolean
from app.core.database import Base
from sqlalchemy.sql import func
import uuid


class Note(Base):
    __tablename__ = "notes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_on = Column(DateTime, default=func.now(), nullable=False)
    updated_on = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Note {self.title} created on {self.created_on}>"
