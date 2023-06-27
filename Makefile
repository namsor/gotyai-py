.PHONY: gen-client

GOTYAI_OPEN_API_PATH ?= http://ns3044521.ip-91-121-222.eu:8080/gotyai/api2/openapi.json

gen-client:
	openapi-generator generate -i $(GOTYAI_OPEN_API_PATH) -g python -o api_client && \
	mv api_client/openapi_client . && \
	rm -rf api_client ;\
