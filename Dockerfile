FROM python:2-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
CMD ["ls"]

CMD ["./run.sh"]

