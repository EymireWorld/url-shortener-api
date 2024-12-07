FROM python:3.12-slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1

COPY . .

RUN pip install --no-cache-dir --requirement /code/requirements.txt
