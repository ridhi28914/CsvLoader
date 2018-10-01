FROM python:2-alpine

# RUN apk update && \
#     apk add --virtual build-deps gcc python-dev musl-dev && \
#     apk add postgresql-dev

# RUN mkdir /code

RUN apk add --update alpine-sdk
WORKDIR /code
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate --noinput

CMD python manage.py runserver 0.0.0.0:8000 --noreload