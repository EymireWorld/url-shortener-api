from pydantic import BaseModel, HttpUrl


class Url(BaseModel):
    url: HttpUrl
