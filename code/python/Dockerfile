FROM python:3.11-slim-bookworm
MAINTAINER johnnylingo
WORKDIR /tmp
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
ENTRYPOINT cd $APP_DIR && uvicorn $APP --app-dir $APP_DIR --host 0.0.0.0 --port $PORT --reload
EXPOSE $PORT/tcp
