FROM python:3.10-buster
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt upgrade -y 

WORKDIR /app/
COPY . .


RUN useradd -s /usr/bin/bash -U webadmin
RUN chown -R webadmin:webadmin /app/ \
    && chmod -R 775 /app/ \
    && mkdir -pm 755 /static_files/ \
    && chown -R webadmin:webadmin /static_files/

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# USER webadmin
