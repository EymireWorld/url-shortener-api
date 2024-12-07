from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.settings import settings


engine = create_async_engine(
    f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}'
)
SessionLocal = async_sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        await session.close()
