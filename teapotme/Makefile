SERVICE = teapotme
HOST := us-docker.pkg.dev
REPO := cloudbuild
REGION := us-central1
PORT := 8080

include Makefile.env

IMAGE = $(HOST)/$(PROJECT_ID)/$(REPO)/$(SERVICE):latest

all: docker gcp-setup gcp-appengine gcp-cloudbuild gcp-cloudrun

docker:
	docker build --tag $(SERVICE) --platform linux/amd64 .

gcp-setup:
	gcloud config set project $(PROJECT_ID)
	gcloud config set core/project $(PROJECT_ID)
	gcloud config set compute/region $(REGION)

gcp-appengine:
	gcloud app deploy ./app.yaml

gcp-cloudbuild:
	gcloud builds submit --tag $(IMAGE) .

gcp-cloudrun:
	gcloud config set run/region $(REGION)
	gcloud run deploy $(SERVICE) --image $(IMAGE) --port $(PORT) --platform=managed --allow-unauthenticated

