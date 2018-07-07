#! /bin/bash

# docker network create imonir
docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d

echo "Starting Frontend"
cd ../imonir.front/
source ./siteup.sh

echo "Starting Backend"
cd ../imonir.back/
source ./siteup.sh

