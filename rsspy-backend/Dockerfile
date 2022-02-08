FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirements.txt ./
RUN apt-get update; apt-get install -y cron vim
RUN pip install -r requirements.txt
COPY . ./