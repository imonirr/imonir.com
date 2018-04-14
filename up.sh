#! /bin/bash

# docker network create imonir

docker-compose -f docker-compose.yml up -d

cd ../imonir.front/
docker-compose -f docker-compose.yml up -d

cd ../imonir.back/ 
docker-compose -f docker-compose.yml up -d

