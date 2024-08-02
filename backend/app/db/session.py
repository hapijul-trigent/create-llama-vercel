from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create a new SQLAlchemy engine
engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True,
)

# Create a configured "Session" class
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency for getting a session
async def get_session():
    async with async_session() as session:
        yield session
