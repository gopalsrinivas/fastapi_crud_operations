from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.note import Note
from app.schemas.note import NoteCreateModel, NoteUpdateModel
from app.core.logging import logger
import uuid


class NoteService:

    @staticmethod
    async def create_note(db: AsyncSession, note_data: NoteCreateModel):
        try:
            new_note = Note(
                id=str(uuid.uuid4()),
                title=note_data.title,
                content=note_data.content,
                is_active=note_data.is_active
            )
            db.add(new_note)
            await db.commit()
            await db.refresh(new_note)

            logger.info(f"Successfully created note: {
                        new_note.id}")  # Log success
            return {"success": True, "note": new_note}
        except Exception as e:
            logger.error(f"Error creating note: {e}")  # Log error
            return {"success": False, "error": "Failed to create note"}

    @staticmethod
    async def get_all_notes(db: AsyncSession, skip: int = 0, limit: int = 10):
        try:
            result = await db.execute(select(Note).offset(skip).limit(limit))
            notes = result.scalars().all()
            logger.info(f"Successfully fetched {len(notes)} notes.")
            return notes
        except Exception as e:
            logger.error(f"Error retrieving notes: {str(e)}")  # Log the error
            raise  # Rethrow the exception

    @staticmethod
    async def get_note_by_id(db: AsyncSession, note_id: str):
        try:
            result = await db.execute(select(Note).filter(Note.id == note_id))
            note = result.scalars().first()
            if not note:
                logger.warning(f"Note with ID {note_id} not found.")  # Log warning
            else:
                logger.info(f"Successfully retrieved note: {
                            note.id}")  # Log success
            return note
        except Exception as e:
            logger.error(f"Error retrieving note {note_id}: {str(e)}")  # Log error
            raise


    @staticmethod
    async def update_note(db: AsyncSession, note_id: str, note_data: NoteUpdateModel):
        try:
            note = await NoteService.get_note_by_id(db, note_id)
            if not note:
                # Log warning
                logger.warning(f"Note with ID {note_id} not found for update.")
                return None
            for var, value in vars(note_data).items():
                if value is not None:
                    setattr(note, var, value)
            await db.commit()
            await db.refresh(note)
            logger.info(f"Successfully updated note: {note.id}")  # Log success
            return note
        except Exception as e:
            logger.error(f"Error updating note {note_id}: {str(e)}")  # Log error
            raise


    @staticmethod
    async def delete_note(db: AsyncSession, note_id: str):
        try:
            note = await NoteService.get_note_by_id(db, note_id)
            if note:
                await db.delete(note)
                await db.commit()
                logger.info(f"Successfully deleted note: {note_id}")  # Log success
                return True
            # Log warning
            logger.warning(f"Note with ID {note_id} not found for deletion.")
            return False
        except Exception as e:
            logger.error(f"Error deleting note {note_id}: {str(e)}")  # Log error
            raise
