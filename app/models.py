from datetime import UTC, datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from app.settings import settings


Base = declarative_base()


class ShortLink(Base):
    __tablename__ = 'short-links'

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str]
    short_url: Mapped[str] = mapped_column(
        String(settings.SHORT_LINK_LENGTH),
        index=True,
    )
    use_count: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(True),
        default=lambda: datetime.now(UTC),
    )
