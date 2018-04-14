#! /bin/bash

docker-compose -f docker-compose.yml down


cd ../imonir.front/
docker-compose -f docker-compose.yml down

cd ../imonir.back/ 
docker-compose -f docker-compose.yml down

