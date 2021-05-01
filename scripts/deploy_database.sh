#!/bin/bash
. ../envr.sh
. ./envr.sh
sudo mkdir -p /mnt/reorchestrator/dbdata
echo -e "import mysql.connector \n"\
"import datetime \n"\
"class Database: \n"\
"  def __init__(self): \n"\
"    self.mydb = mysql.connector.connect( \n"\
"      host=\""$mysql_ip"\",\n"\
"      user=\""$mysql_username"\",\n"\
"      password=\""$mysql_password"\",\n"\
"      port=\""$mysql_port"\",\n"\
"      database=\""$mysql_database"\"\n"\
"      )\n"\
"    self.cursor = self.mydb.cursor()\n"\
"  def select(self, query):\n"\
"    self.cursor.execute(query)\n"\
"    return self.cursor\n"\
"  def insert(self, query):\n"\
"    self.cursor.execute(query)\n"\
"    added_row_id = self.cursor.lastrowid\n"\
"    self.mydb.commit()\n"\
"    return added_row_id\n"\
"  def close(self):\n"\
"    self.cursor.close()\n"\
"    self.mydb.close()\n"\
" \n"\
" \n"\
" \n" > MYsql.py
echo "mysql_root_password:"$mysql_root_password
kubectl create secret generic orch-mysql-secret --from-literal=MYSQL_ROOT_PASSWORD=$mysql_root_password --from-literal=MYSQL_DATABASE=$mysql_database --from-literal=MYSQL_USER=$mysql_username --from-literal=MYSQL_PASSWORD=$mysql_password


echo -e "apiVersion: apps/v1 \n"\
"kind: Deployment \n"\
"metadata: \n"\
"  name: reorch-mysql-deployment \n"\
"  labels: \n"\
"    app: reorch-mysql \n"\
"spec: \n"\
"  replicas: 1 \n"\
"  selector: \n"\
"    matchLabels: \n"\
"      app: reorch-mysql \n"\
"  template: \n"\
"    metadata: \n"\
"      labels: \n"\
"        app: reorch-mysql \n"\
"    spec: \n"\
"      containers: \n"\
"        - name: mysql57 \n"\
"          image: mysql:5.7 \n"\
"          ports: \n"\
"            - containerPort: 3306 \n"\
"          volumeMounts: \n"\
"            - mountPath: \"/var/lib/mysql\" \n"\
"              name: reorch-mysql-data \n"\
"          env: \n"\
"            - name: MYSQL_ROOT_PASSWORD \n"\
"              valueFrom: \n"\
"                secretKeyRef: \n"\
"                  name: orch-mysql-secret \n"\
"                  key: MYSQL_ROOT_PASSWORD \n"\
"            - name: MYSQL_DATABASE \n"\
"              valueFrom: \n"\
"                secretKeyRef: \n"\
"                  name: orch-mysql-secret \n"\
"                  key: MYSQL_DATABASE \n"\
"            - name: MYSQL_USER \n"\
"              valueFrom: \n"\
"                secretKeyRef: \n"\
"                  name: orch-mysql-secret \n"\
"                  key: MYSQL_USER \n"\
"            - name: MYSQL_PASSWORD \n"\
"              valueFrom: \n"\
"                secretKeyRef: \n"\
"                  name: orch-mysql-secret \n"\
"                  key: MYSQL_PASSWORD \n"\
"      volumes: \n"\
"        - name: reorch-mysql-data \n"\
"          hostPath: \n"\
"            path: /mnt/reorchestrator/dbdata \n"\
"            type: DirectoryOrCreate \n"\
"--- \n"\
"apiVersion: v1 \n"\
"kind: Service \n"\
"metadata: \n"\
"  name: reorch-mysql-service \n"\
"spec: \n"\
"  ports: \n"\
"    - name: orchmysqlportname \n"\
"      port: 3306 \n"\
"      targetPort: 3306 \n"\
"      protocol: TCP \n"\
"      nodePort: "$mysql_port" \n"\
"  type: NodePort \n"\
"  selector: \n"\
"    app: reorch-mysql \n" > mysql5-7-deployment.yml


kubectl apply -f mysql5-7-deployment.yml

echo "# Creating database tables..."
python3 ./scripts/create_tables.py
