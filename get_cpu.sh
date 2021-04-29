#!/bin/sh
kubectl top pod -n jitsi | grep $1 | awk '{print $2}'