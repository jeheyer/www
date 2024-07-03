#FROM debian:bookworm-slim
FROM python:3.12-slim-bookworm
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt -y install python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN rm -Rf /var/lib/apt/lists/*
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PORT=8000
ENV APP_DIR=/opt/www/code/python
ENV APP=app:app
RUN mkdir -p $APP_DIR
COPY *.py $APP_DIR/
RUN mkdir -p /opt/db
COPY *.mmdb /opt/db/
RUN mkdir -p /opt/private
COPY *.toml /opt/private/
ENTRYPOINT cd $APP_DIR && uvicorn $APP --app-dir $APP_DIR --host 0.0.0.0 --port $PORT --reload
EXPOSE $PORT/tcp
