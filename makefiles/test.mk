test-unit: ##@Global install dependencies
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
  	-u ${UID_LOCAL}:${GID_LOCAL} \
		${IMAGE_DEV} \
		yarn run test

test-integration: ##@Global install dependencies
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-v  ~/.aws/:/app/.aws/:rw \
  	-u ${UID_LOCAL}:${GID_LOCAL} \
  	-e HOME='/app' \
    -e AWS_SDK_LOAD_NONDEFAULT_CONFIG='1' \
    -e AWS_CONFIG_FILE='/app/.aws/config' \
    -e AWS_PROFILE='dev' \
    -e AWS_SDK_LOAD_CONFIG='1' \
		--network="neo_network" \
		${IMAGE_DEV} \
		yarn run test:e2e

test-bdd: ##@Global Unit test
	@docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}":/${APP_DIR} \
		-v  ~/.aws/:/app/.aws/:rw \
		-u ${UID_LOCAL}:${GID_LOCAL} \
		-e HOME='/app' \
		-e AWS_SDK_LOAD_NONDEFAULT_CONFIG='1' \
		-e AWS_CONFIG_FILE='/app/.aws/config' \
		-e AWS_PROFILE='dev' \
		-e AWS_SDK_LOAD_CONFIG='1' \
		--network="neo_network" \
		${IMAGE_DEV} \
		yarn bdd

test-deploy: ##@Global Test deploy
	docker container run --workdir "/${APP_DIR}" --rm -i \
		-v "${PWD}/${APP_DIR}/coverage":/${APP_DIR}/coverage \
		${IMAGE_DEPLOY_TEST} \
		yarn test
