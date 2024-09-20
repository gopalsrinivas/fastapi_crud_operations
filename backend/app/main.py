from fastapi import FastAPI
from app.routers import note
import uvicorn
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import logger

# Load logging configuration
import app.core.logging

app = FastAPI(
    title="FastAPI CRUD Operations 1",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure the router is included correctly
app.include_router(note.router, prefix="/api/notes", tags=["notes"])
