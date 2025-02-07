#FROM python:3.11-slim-bookworm
#ARG DEBIAN_FRONTEND=noninteractive
#RUN apt update && apt upgrade -y
#RUN rm -Rf /var/lib/apt/lists/*
FROM python:3.12-alpine
MAINTAINER johnnylingo
WORKDIR /tmp
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENV PORT=8000
ENV APP_DIR=/opt/www/code/python
ENV APP=app:app
RUN mkdir -p $APP_DIR
COPY *.py $APP_DIR/
RUN mkdir -p /opt/db
COPY *.mmdb /opt/db/
RUN mkdir -p /opt/private
RUN mkdir -p /opt/private/cfg
COPY *.toml /opt/private/cfg/
ENTRYPOINT cd $APP_DIR && uvicorn $APP --app-dir $APP_DIR --host 0.0.0.0 --port $PORT --reload
#ENTRYPOINT ["pip", "list"]
EXPOSE $PORT/tcp
