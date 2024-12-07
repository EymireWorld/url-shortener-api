from fastapi import APIRouter

from .url.router import router as url_router


router = APIRouter(prefix='/api')
router.include_router(url_router, prefix='/url')
