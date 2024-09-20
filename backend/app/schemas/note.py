from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class NoteModel(BaseModel):
    id: str
    title: str
    content: str
    is_active: bool
    created_on: datetime
    updated_on: Optional[datetime] = None

    class Config:
        model_config = ConfigDict(
            from_attributes=True
        )


class NoteCreateModel(BaseModel):
    title: str
    content: str
    is_active: bool = True
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Sample title",
                "content": "Sample content",
                "is_active": True 
            }
        }


class NoteUpdateModel(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True
