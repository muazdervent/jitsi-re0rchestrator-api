#!/bin/bash
echo "# Setup starting..."

echo "# Requirements installing..."
sudo ./scripts/requirements.sh

echo "# Database deploying..."
./scripts/deploy_database.sh

echo "# Creating jitsi namespace..."
kubectl create ns jitsi

echo "# Creating jitsi envirenment configMap..."
kubectl apply -f ./deployments/jitsi-env.yml

echo "# Creating metric server..."
kubectl apply -f ./deployments/metric-server.yml

echo "# Creating jibri finalize script..."
sudo ./scripts/create_jibri_finalize.sh

sudo mkdir -p /mnt/reorchestrator
sudo mv jitsi-data /mnt/reorchestrator

cd express
npm init
npm i -s express.js

#sudo forever start express.js

cd ..
#nohup ./cleaner.sh &

