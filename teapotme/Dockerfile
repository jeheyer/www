FROM python:3.8.2-alpine
MAINTAINER johnnylingo
RUN ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /tmp
COPY ./requirements.txt ./
RUN apk add build-base linux-headers
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
ENV PORT=8080
ENV WSGI_DIR=/opt
ENV WSGI_FILE=wsgi.py
COPY $WSGI_FILE $WSGI_DIR
ENTRYPOINT cd $WSGI_DIR && uwsgi --http :$PORT --workers 3 --wsgi-file $WSGI_FILE --callable application --enable-threads
EXPOSE $PORT
