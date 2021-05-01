# Jitsi reOrchestrator API

Jitsi reOrchestartor API for Kubernetes. The purpose of this API is to run and manage more than one Jitsi-Meet on a kubernetes cluster.


## Architecture

![architecture_image](https://github.com/muazdervent/jitsi-reorchestrator-api/blob/master/architecture_image.png?raw=true)

## Installation and explanation

It is **assumed** that kubernetes and python3 are **installed**.

All steps must be run on the **master node.**


What to install:
```bash
pip3 install mysql-connector-python
sudo apt-get install mysql-client
```

Clone the repository:

```bash
$ git clone https://github.com/muazdervent/jitsi-reorchestrator-api.git
```


First deploy kubernetes  metric server:
```bash
$ cd jitsi-reochestrator-api/deployments
$ kubectl apply -f metric-server.yml
```

Create jitsi namespace:

```bash
$ kubectl create ns jitsi
```


Deploy mysql node, you can change mysql password in secret:

(Examine the yml file and change the location marked with ## as desired.)

```bash
$ sudo mkdir -p /mnt/reorchestrator/mysql-data

$ kubectl create secret generic orch-mysql-secret --from-literal=MYSQL_ROOT_PASSWORD=root --from-literal=MYSQL_DATABASE=reorchestrator --from-literal=MYSQL_USER=root

$ kubectl apply -f mysql-deployment.yml 
```

- finalize.sh daki mysql parametrelerini degistir
- jitsi ns ini olusturmayi unutma
- metric server deploy et
- mysql deploy edilmesi (secret olusturmayı unutma)
- MYsql.py dosyasını düzenleme