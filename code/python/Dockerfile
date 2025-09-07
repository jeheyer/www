FROM debian:trixie-slim
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /tmp
COPY ./requirements.txt ./
RUN apt update && apt install -y python3-full python3-pip
#RUN pip install setuptools wheel --break-system-packages
RUN pip install -r requirements.txt --break-system-packages
RUN apt clean && rm -Rf /var/lib/apt/lists/*
ENV PORT=8000
ENV APP_DIR=/opt/www/code/python
ENV APP=app:app
RUN mkdir -p $APP_DIR
COPY *.py $APP_DIR/
RUN mkdir -p /opt/db
#COPY *.mmdb /opt/db/
RUN mkdir -p /opt/private
RUN mkdir -p /opt/private/cfg
#COPY *.toml /opt/private/cfg/
#ENTRYPOINT ["pip", "list"]
ENTRYPOINT cd $APP_DIR && uvicorn $APP --app-dir $APP_DIR --host 0.0.0.0 --port $PORT --reload
#ENTRYPOINT cd $APP_DIR && hypercorn -b 0.0.0.0:$PORT -w 1 --access-logfile '-' $APP
EXPOSE $PORT/tcp
