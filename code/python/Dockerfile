FROM debian:trixie-slim
ARG DEBIAN_FRONTEND=noninteractive
ENV PORT=8000
ENV APP_DIR=/opt/www/code/python
ENV APP=app:app
ENV CFG_DIR=/opt/private/cfg
ENV DB_DIR=/opt/db
WORKDIR /tmp
RUN apt update && apt install -y python3-full python3-pip
##COPY ./requirements.txt ./
RUN pip install -r requirements.txt --break-system-packages
#COPY ./pyproject.toml ./
#RUN pip install . --break-system-packages
RUN apt clean && rm -Rf /var/lib/apt/lists/*
RUN mkdir -p $APP_DIR
COPY *.py $APP_DIR/
#RUN mkdir -p $DB_DIR
#COPY *.mmdb $DB_DIR/
#RUN mkdir -p $CFG_DIR
#COPY *.toml $CFG_DIR/
#ENTRYPOINT cd $APP_DIR && hypercorn -b 0.0.0.0:$PORT -w 1 --access-logfile '-' $APP
ENTRYPOINT cd $APP_DIR && uvicorn $APP --app-dir $APP_DIR --host 0.0.0.0 --port $PORT --reload
EXPOSE $PORT/tcp
