cp docker/Dockerfile .

IMAGE_NAME="nexus-4"
IMAGE_TAG="latest"

docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .


rm Dockerfile
