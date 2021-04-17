FROM python:3.9


RUN pip install --upgrade pipenv

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV WORKDIR /app

WORKDIR /app


ADD . /app

RUN pipenv install --system --deploy


