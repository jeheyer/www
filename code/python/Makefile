HOST := gcr.io
REGION := us-central1
PROJECT_ID := my-project
REPO := my-repo
SERVICE := python

include Makefile.env

all: gcp-setup cloud-build cloud-run-deploy

gcp-setup:
	gcloud config set project $(PROJECT_ID)

cloud-build:
	#gcloud auth configure-docker $(HOST)
	#gcloud builds submit --tag gcr.io/$(PROJECT_ID)/$(SERVICE_NAME) .
	gcloud builds submit --tag $(HOST)/$(PROJECT_ID)/$(REPO)/$(SERVICE):latest .

cloud-run-deploy:
	gcloud config set run/region $(REGION)
	#gcloud run deploy $(SERVICE_NAME) --image gcr.io/$(GCP_PROJECT_ID)/$(SERVICE_NAME) --allow-unauthenticated
	gcloud run deploy $(SERVICE) --image $(HOST)/$(PROJECT_ID)/$(REPO)/$(SERVICE):latest
