import os
import logging
from alembic import command
from alembic.config import Config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Inspector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.core.config import settings
from sqlalchemy import text
from app.routers import note

# Database URL with async driver
db_url = settings.DATABASE_URL.replace(
    "postgresql://", "postgresql+asyncpg://")


async def run_alembic_migrations():
    alembic_cfg = Config(os.path.join(
        os.path.dirname(__file__), "../../alembic.ini"))
    async_engine = create_async_engine(db_url, future=True)
    async_session = sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession)

    async with async_engine.connect() as connection:
        result = await connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public';"))
        existing_tables = [row[0] for row in result]

        has_changes = "notes" not in existing_tables

        if has_changes:
            try:
                command.revision(alembic_cfg, autogenerate=True,
                                 message="Auto migration on startup")
                command.upgrade(alembic_cfg, "head")
            except Exception as e:
                logging.error(f"Alembic migration failed: {e}")
                raise
        else:
            logging.info("No schema changes detected; skipping migration.")

app = FastAPI(
    title="FastAPI CRUD Operations",
    docs_url="/api_v1/docs",
    redoc_url="/api_v1/redoc",
)

@app.on_event("startup")
async def startup_event():
    await run_alembic_migrations()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(note.router, prefix="/api/notes", tags=["notes"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
