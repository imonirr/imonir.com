#! /bin/bash

# docker network create imonir

docker-compose up -d

echo "Starting Frontend"
cd ../imonir.front/
source ./up.sh

echo "Starting Backend"
cd ../imonir.back/
source ./up.sh

