from fastapi import HTTPException, status
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.url.dependencies import generate_short_link
from app.models import ShortLink


async def get_short_url(
    session: AsyncSession,
    original_url: str,
) -> str:
    stmt = select(ShortLink).where(ShortLink.original_url == original_url)
    result = await session.execute(stmt)
    result = result.scalar()

    if result:
        return result.short_url

    short_url = await generate_short_link(session)

    stmt = insert(ShortLink).values(
        original_url=original_url,
        short_url=short_url,
    )
    result = await session.execute(stmt)
    await session.commit()

    return short_url


async def get_original_url(
    session: AsyncSession,
    short_url: str,
) -> str:
    stmt = select(ShortLink).where(ShortLink.short_url == short_url)
    result = await session.execute(stmt)
    result = result.scalar()

    if result:
        stmt = (
            update(ShortLink)
            .values(use_count=result.use_count + 1)
            .where(ShortLink.id == result.id)
        )
        await session.execute(stmt)
        await session.commit()

        return result.original_url

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Url not found.',
    )
