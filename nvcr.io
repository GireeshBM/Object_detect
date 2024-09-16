#!/bin/bash

# Log out from nvcr.io
docker logout nvcr.io

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
else
    echo "Docker is installed."
fi

# Check if Docker daemon is running
if ! sudo systemctl is-active --quiet docker; then
    echo "Docker daemon is not running. Please start Docker."
    exit 1
else
    echo "Docker daemon is running."
fi

# Set Docker registry and retrieve API key from JSON file
DOCKER_REGISTRY="nvcr.io"
API_KEY_FILE="/home/satyaki/api_key_docker.json"

# Check if the JSON file exists
if [ ! -f "$API_KEY_FILE" ]; then
    echo "API key file not found: $API_KEY_FILE"
    exit 1
fi

# Extract the API key from the JSON file
NEW_API_KEY=$(jq -r '.NEW_API_KEY' "$API_KEY_FILE")

if [ -z "$NEW_API_KEY" ]; then
    echo "Failed to retrieve the API key from $API_KEY_FILE"
    exit 1
else
    echo "API key retrieved successfully."
fi

# Log in to Docker registry using --password-stdin
echo "$NEW_API_KEY" | docker login $DOCKER_REGISTRY -u '$oauthtoken' --password-stdin

if [ $? -ne 0 ]; then
    echo "Docker login to $DOCKER_REGISTRY failed. Please check your credentials."
    exit 1
else
    echo "Docker login to $DOCKER_REGISTRY succeeded."
fi

/home/satyaki/api_key_docker.json
{
    "NEW_API_KEY": "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"
}
