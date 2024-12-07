from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.dependencies import session_dep

from . import services
from .schemas import Url


router = APIRouter()


@router.get('/{short_url}')
async def get_original_link(
    session: session_dep,
    short_url: str,
) -> RedirectResponse:
    url = await services.get_original_url(session, short_url)

    return RedirectResponse(url)


@router.post('')
async def get_short_link(
    request: Request,
    session: session_dep,
    data: Url,
) -> Url:
    url = await services.get_short_url(session, str(data.url).rstrip('/'))

    return Url(url=str(request.base_url).rstrip('/') + '/api/url/' + url)  # type: ignore
