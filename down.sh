#! /bin/bash

docker-compose down

echo "Stopping Frontend"
cd ../imonir.front/
source ./down.sh

echo "Stoping Backend"
cd ../imonir.back/
source ./down.sh

