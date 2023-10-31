FROM python:3.10.5

EXPOSE 8000
RUN mkdir /project
WORKDIR /project

RUN apt-get update && apt-get install -y libpq-dev

COPY requirements.txt /project
RUN pip install -r requirements.txt

COPY ./project /project

CMD gunicorn    --bind 0.0.0.0:8000        \
                --reload wsgi:application

