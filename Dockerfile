FROM python:3.10-rc-buster
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt upgrade -y 

WORKDIR /app/

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
