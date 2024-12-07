import random
import string

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ShortLink
from app.settings import settings


CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits


async def generate_short_link(session: AsyncSession):
    while True:
        short_url = ''.join(random.choice(CHARACTERS) for _ in range(settings.SHORT_LINK_LENGTH))

        stmt = select(ShortLink).where(ShortLink.short_url == short_url)
        result = await session.execute(stmt)

        if not result.scalar():
            return short_url
