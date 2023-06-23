echo update openapi-generator
./bin/utils/openapi-generator-cli.sh
rm -Rf ./gotyai/client/python/*
echo run openapi-generator
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate  --git-repo-id gotyai-py --git-user-id namsor --skip-validate-spec -i http://ns3044521.ip-91-121-222.eu:8080/gotyai/api2/openapi.json -g python -o  gotyai/client/python  --additional-properties packageVersion=3.0.2 --additional-properties packageName=gotyai_client
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0.jar namsor-sdk2-1.0.0.jar
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0-javadoc.jar namsor-sdk2-1.0.0-javadoc.jar
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0-sources.jar namsor-sdk2-1.0.0-sources.jar
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0-tests.jar namsor-sdk2-1.0.0-tests.jar
cp -R /home/namsor/codegen/openapi-generator/gotyai/client/python/* /home/namsor/codegen/gotyai-py/
cp /home/namsor/codegen/openapi-generator/gotyai-run-python.bash /home/namsor/codegen/gotyai-py/


