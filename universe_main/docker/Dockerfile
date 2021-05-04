FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV WORKDIR /app

WORKDIR /app

ADD . /app


RUN pip install pipenv --upgrade --no-cache-dir

RUN pipenv install --system --deploy --dev



#See more details in wheels/README.txt
RUN cp wheels/django-rest-swagger/index.html /usr/local/lib/python3.9/site-packages/rest_framework_swagger/templates/rest_framework_swagger

