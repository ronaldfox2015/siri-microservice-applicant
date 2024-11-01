## CONTAINER VARS ##
USERNAME_LOCAL ?= "$(shell whoami)"
UID_LOCAL      ?= "$(shell id -u)"
GID_LOCAL      ?= "$(shell id -g)"

IMAGE_BUILD     = $(PROJECT_NAME):$(ENV)
CONTAINER_NAME  = $(PROJECT_NAME)_backend

DEV_TAG         ?= $(ENV)
IMAGE_DEV       = $(PROJECT_NAME):$(DEV_TAG)
PREFIX_PATH     = /$(VERSION)/$(SERVICE_NAME)
VIRTUAL_HOST	= /$(VERSION)/$(SERVICE_NAME)*
MODE			= image
IMAGE_DEPLOY_DEV = $(PROJECT_NAME):$(ENV)
IMAGE_DEPLOY_TEST = $(PROJECT_NAME)-test:$(ENV)

YARN_ENVIRONMENT ?=

build:##@Global Build project : make build MODE=image, make build MODE=build-dist
	docker build --build-arg UID=$(USER_ID) --build-arg GID=$(GROUP_ID) -f docker/dev/Dockerfile --no-cache -t $(IMAGE_BUILD)  ./

build-image-test: ##@Global Create a Docker image with the dependencies packaged
	@docker build -f docker/test/Dockerfile --no-cache -t $(IMAGE_DEPLOY_TEST) .

install: ##@Global install dependencies : make install YARN_ENVIRONMENT=""
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		${IMAGE_DEPLOY_DEV} \
		yarn install $(YARN_ENVIRONMENT)

compile-proto: ##@Global install dependencies
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		${IMAGE_DEPLOY_DEV} \
		sh compile.proto.sh

up: ##@Local Start the project
	IMAGE_DEV=$(IMAGE_DEPLOY_DEV) \
	CONTAINER_NAME=$(CONTAINER_NAME) \
	PATH_SERVICE=$(PATH_SERVICE) \
	NETWORK=${DOCKER_NETWORK} \
	docker compose -p $(SERVICE_NAME) up backend

down: ##@Local Stops and removes the docker containers: make down
	@docker rm -f $(CONTAINER_NAME)

log: ##@Local Show project logs
	@docker logs -f $(CONTAINER_NAME)


hooks-app: ##@Local hooks the project
	cp $(PWD)/hooks/pre-commit .git/hooks/ && chmod +x .git/hooks/pre-commit
	cp $(PWD)/hooks/prepare-commit-msg .git/hooks/ && chmod +x .git/hooks/prepare-commit-msg

ssh: ##@Local Access the docker container
	@docker exec -it  $(CONTAINER_NAME) /bin/sh

lint: ##@Global install dependencies
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
  	-u ${UID_LOCAL}:${GID_LOCAL} \
		${IMAGE_DEPLOY_DEV} \
		yarn lint


doc: ##@Global Build project
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-p 8080:8080 \
		${IMAGE_DEPLOY_DEV} \
		yarn doc

sync-container-config: ##@Deploy Sync configs files from S3
	aws s3 sync s3://$(INFRA_BUCKET)/config/container/$(OWNER)/$(ENV)/$(SERVICE_NAME)/ app/ --profile ${ACCOUNT_ENV}

push-container-config: ##@Deploy Sync configs files from S3
	aws s3 cp app/.env s3://$(INFRA_BUCKET)/config/container/$(OWNER)/$(ENV)/$(SERVICE_NAME)/.env --profile ${ACCOUNT_ENV}

container-upload-app-config: ##@Deploy Sync configs files from S3
	@aws s3 cp app/.env s3://$(INFRA_BUCKET)/config/container/$(OWNER)/$(ENV)/$(SERVICE_NAME)/ --profile ${ENV}
