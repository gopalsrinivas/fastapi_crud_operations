from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.note import NoteModel, NoteCreateModel, NoteUpdateModel
from app.core.database import get_db
from app.services.note import NoteService
from app.core.logging import logger


router = APIRouter()

@router.post("/", response_model=NoteModel)
async def create_note(note_data: NoteCreateModel, db: AsyncSession = Depends(get_db)):
    response = await NoteService.create_note(db=db, note_data=note_data)

    if response.get("success"):
        logger.info(f"Note created successfully: {response['note'].id}")
        return response["note"]
    else:
        logger.error(f"Failed to create note: {response['error']}")
        raise HTTPException(status_code=500, detail=response["error"])


@router.get("/", response_model=List[NoteModel])
async def get_notes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    try:
        notes = await NoteService.get_all_notes(db=db, skip=skip, limit=limit)
        logger.info(f"Successfully retrieved {len(notes)} notes.")  # Log success
        return notes
    except Exception as e:
        logger.error(f"Failed to retrieve notes: {str(e)}")  # Log the error
        raise HTTPException(status_code=500, detail="Failed to retrieve notes")


@router.get("/{note_id}", response_model=NoteModel)
async def get_note(note_id: str, db: AsyncSession = Depends(get_db)):
    try:
        note = await NoteService.get_note_by_id(db=db, note_id=note_id)
        if not note:
            logger.warning(f"Note with ID {note_id} not found.")  # Log warning
            raise HTTPException(status_code=404, detail="Note not found")
        logger.info(f"Successfully retrieved note: {note.id}")  # Log success
        return note
    except Exception as e:
        logger.error(f"Error retrieving note {note_id}: {str(e)}")  # Log error
        raise HTTPException(status_code=500, detail="Failed to retrieve note")


@router.put("/{note_id}", response_model=NoteModel)
async def update_note(note_id: str, note_data: NoteUpdateModel, db: AsyncSession = Depends(get_db)):
    try:
        updated_note = await NoteService.update_note(db=db, note_id=note_id, note_data=note_data)
        if not updated_note:
            # Log warning
            logger.warning(f"Note with ID {note_id} not found for update.")
            raise HTTPException(status_code=404, detail="Note not found")
        logger.info(f"Successfully updated note: {
                    updated_note.id}")  # Log success
        return updated_note
    except Exception as e:
        logger.error(f"Error updating note {note_id}: {str(e)}")  # Log error
        raise HTTPException(status_code=500, detail="Failed to update note")


@router.delete("/{note_id}")
async def delete_note(note_id: str, db: AsyncSession = Depends(get_db)):
    try:
        success = await NoteService.delete_note(db=db, note_id=note_id)
        if not success:
            # Log warning
            logger.warning(f"Note with ID {note_id} not found for deletion.")
            raise HTTPException(status_code=404, detail="Note not found")
        logger.info(f"Successfully deleted note: {note_id}")  # Log success
        return {"message": "Note deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting note {note_id}: {str(e)}")  # Log error
        raise HTTPException(status_code=500, detail="Failed to delete note")
