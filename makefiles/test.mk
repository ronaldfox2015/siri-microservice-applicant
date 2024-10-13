test-deploy:
	rm -f app/.coverage
	cp app/requirements.txt docker/test/resources/requirements.txt
	docker build -f docker/test/Dockerfile \
				-t ${IMAGE_TEST} docker/test/
	rm -f docker/test/resources/requirements.txt
	docker run --rm -t -u $(UID_LOCAL):$(GID_LOCAL) \
			-v $(PWD)/app:/app:rw -v $(PWD)/docker/test/config:/app/config:rw $(IMAGE_TEST)
	rm -rf app/config
	sed -i 's|/app/|app/|g' $(PWD)/app/build/reports/cover/xml/coverage.xml
	sed -i '/<line number="0"/d' $(PWD)/app/build/reports/cover/xml/coverage.xml

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


