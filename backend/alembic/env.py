from app.core.database import Base
import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Alembic Config object
config = context.config

# Update sqlalchemy.url from the environment variable
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your models' MetaData object for Alembic to use
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True,
        dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        pool_pre_ping=True,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(context.configure, connection=connection, target_metadata=target_metadata)

        async with connection.begin() as transaction:
            await context.run_migrations()


def run_async_migrations():
    """Helper to run migrations considering event loop status."""
    try:
        # Check if an event loop is already running
        loop = asyncio.get_running_loop()
    except RuntimeError:  # No event loop, so we can run it normally
        asyncio.run(run_migrations_online())
    else:  # Already running, use loop to create a task
        loop.create_task(run_migrations_online())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_async_migrations()
