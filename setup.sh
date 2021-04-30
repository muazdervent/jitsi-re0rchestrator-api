#!/bin/bash
echo "# Setup starting..."

echo "# Requirements installing..."
./scripts/requirements.sh

echo "# Database deploying..."
./scripts/deploy_database.sh

echo "# Creating jitsi namespace..."
kubectl create ns jitsi

echo "# Creating jitsi envirenment configMap..."
kubectl apply -f ./deployments/jitsi-env.yml

echo "# Creating jibri finalize script..."
./scripts/create_jibri_finalize.sh

mv jitsi-data /mnt/reorchestrator

forever start express.js

nohup ./cleaner.sh &

