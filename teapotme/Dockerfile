FROM python:3.12-alpine
MAINTAINER johnnylingo
WORKDIR /tmp
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --break-system-packages
ENV PORT=8080
ENV WSGI_DIR=/opt
ENV WSGI_APP=wsgi:application
COPY main.py $WSGI_DIR
COPY wsgi.py $WSGI_DIR
ENTRYPOINT gunicorn -b 0.0.0.0:$PORT -w 3 --access-logfile '-' --chdir $WSGI_DIR $WSGI_APP
EXPOSE $PORT/tcp
