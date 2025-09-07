# teapotme
Souce Code for teapotme.com - a python wsgi app that returns a 418 status code

## Running on Docker

```
docker build -t teapotme .
docker run -p 32768:8080 teapotme
```

## Running on Google Cloud Run

```
gcloud builds submit --tag gcr.io/<PROJECT_ID>/teapotme
gcloud config set run/region us-central1
gcloud run deploy teapotme --image gcr.io/<PROJECT_ID>/teapotme --allow-unauthenticated --port=8080
```

## Deploying on Google App Engine

```
gcloud app deploy
```
