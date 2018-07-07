#! /bin/bash

# docker network create imonir
docker-compose -f docker-compose.yml -f docker-compose.production.yml down -d

echo "Starting Frontend"
cd ../imonir.front/
source ./sitedown.sh

echo "Starting Backend"
cd ../imonir.back/
source ./sitedown.sh

