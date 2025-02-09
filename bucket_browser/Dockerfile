FROM python:3.11-slim-bullseye
ENV PORT=8080
ENV APP_DIR=/opt
ENV APP_APP=wsgi:app
WORKDIR /tmp
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY wsgi.py $APP_DIR/
COPY templates/ $APP_DIR/templates/
COPY static/ $APP_DIR/static/
ENTRYPOINT gunicorn -b 0.0.0.0:$PORT -w 1 --access-logfile '-' --chdir $APP_DIR $APP_APP
EXPOSE $PORT
