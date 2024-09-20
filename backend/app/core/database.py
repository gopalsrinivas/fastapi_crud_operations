from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Set up database engine and session
engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base class for models
Base = declarative_base()

# Dependency for getting the session


async def get_db():
    async with SessionLocal() as session:
        yield session

# Just return the database URL if needed


def get_db_url():
    return settings.DATABASE_URL
