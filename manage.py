import os
import mysql.connector
import time
from MYsql import * 
import sys

args = sys.argv





def log_ekle(log_string):
  with open("main-machine-py-logs.txt", "a") as a_file:
    a_file.write(log_string  +"  "+ str(datetime.datetime.now()) )
    a_file.write("\n")


def dosya_olustur(web_port_number,session_uniq_id):

  dosya_adi = "orch-deployment.yml"
  k8sapp = "jitsi-"+str(web_port_number)
  name = "jitsi-"+str(web_port_number)

  jvbServicePort = str(int(web_port_number) + 200) # 30400 ile 30599 arası olacak
  jvbServiceName = "jvb-udp-"+str(int(web_port_number) + 200)

  webServicePort = str(web_port_number) # 30200 ile 30399 arası olacak
  webServiceName = "web-"+str(web_port_number)


  dosya = open(dosya_adi, 'w',encoding="utf-8") 
  satir1 ="\n"\
  "apiVersion: apps/v1\n"\
  "kind: Deployment\n"\
  "metadata:\n"\
  "  labels:\n"\
  "    k8s-app: "+k8sapp+"\n"\
  "  name: "+name+"\n"\
  "  namespace: jitsi\n"\
  "spec:\n"\
  "  replicas: 1\n"\
  "  strategy:\n"\
  "    type: Recreate\n"\
  "  selector:\n"\
  "    matchLabels:\n"\
  "      k8s-app: "+k8sapp+"\n"\
  "  template:\n"\
  "    metadata:\n"\
  "      labels:\n"\
  "        k8s-app: "+k8sapp+"\n"\
  "    spec:\n"\
  "      hostAliases:\n"\
  "        - ip: '127.0.0.1'\n"\
  "          hostnames:\n"\
  "            - example.com\n"\
  "      containers:\n"\
  "        - name: web\n"\
  "          image: docker.io/jitsi/web:stable-4857\n"\
  "          resources:\n"\
  "            limits:\n"\
  "              cpu: '1000m'\n"\
  "              memory: 1024Mi\n"\
  "            requests:\n"\
  "              cpu: '200m'\n"\
  "              memory: '50Mi'\n"\
  "          envFrom:\n"\
  "            - configMapRef:\n"\
  "                name: jitsi-env-moodle\n"\
  "          volumeMounts:\n"\
  "            - mountPath: /config\n"\
  "              name: web-config\n"\
  "            - mountPath: /usr/share/jitsi-meet/images\n"\
  "              name: web-images\n"\
  "        - name: jicofo\n"\
  "          image: docker.io/jitsi/jicofo:stable-4857\n"\
  "          resources:\n"\
  "            limits:\n"\
  "              cpu: '500m'\n"\
  "              memory: 1024Mi\n"\
  "            requests:\n"\
  "              cpu: '100m'\n"\
  "              memory: 256Mi\n"\
  "          envFrom:\n"\
  "            - configMapRef:\n"\
  "                name: jitsi-env-moodle\n"\
  "        - name: prosody\n"\
  "          image: docker.io/jitsi/prosody:stable-4857\n"\
  "          args: ['/scriptss/./script.sh']\n"\
  "          resources:\n"\
  "            limits:\n"\
  "              cpu: '1000m'\n"\
  "              memory: '1024Mi'\n"\
  "            requests:\n"\
  "              cpu: '50m'\n"\
  "              memory: '128Mi'\n"\
  "          env:\n"\
  "            - name: H_NAME\n"\
  "              value: 'root'\n"\
  "            - name: H_PASSW\n"\
  "              value: 'rootpassword'\n"\
  "          envFrom:\n"\
  "            - configMapRef:\n"\
  "                name: jitsi-env-moodle\n"\
  "          volumeMounts:\n"\
  "            - mountPath: /scriptss\n"\
  "              name: prosody-script\n"\
  "        - name: jvb\n"\
  "          image: docker.io/jitsi/jvb:stable-4857\n"\
  "          resources:\n"\
  "            limits:\n"\
  "              cpu: '4000m'\n"\
  "              memory: '2560Mi'\n"\
  "            requests:\n"\
  "              cpu: '500m'\n"\
  "              memory: '512Mi'\n"\
  "          env:\n"\
  "            - name: JVB_PORT\n"\
  "              value: '"+jvbServicePort+"'\n"\
  "          envFrom:\n"\
  "            - configMapRef:\n"\
  "                name: jitsi-env-moodle\n"\
  "        - name: jibri\n"\
  "          image: docker.io/mdervent/izuzem-jibri:v1.1\n"\
  "          resources:\n"\
  "            limits:\n"\
  "              cpu: '3000m'\n"\
  "              memory: '8192Mi'\n"\
  "            requests:\n"\
  "              cpu: '500m'\n"\
  "              memory: '2048Mi'\n"\
  "          env:\n"\
  "            - name: SESSION_UNIQ_ID\n"\
  "              value: '"+str(session_uniq_id)+"'\n"\
  "          envFrom:\n"\
  "            - configMapRef:\n"\
  "                name: jitsi-env-moodle\n"\
  "          securityContext:\n"\
  "            privileged: true\n"\
  "            capabilities:\n"\
  "              add:\n"\
  "                - NET_BIND_SERVICE\n"\
  "                - SYS_ADMIN\n"\
  "          volumeMounts:\n"\
  "            - mountPath: /dev/snd\n"\
  "              name: dev-snd\n"\
  "            - mountPath: /dev/shm\n"\
  "              name: dev-shm\n"\
  "            - mountPath: /config\n"\
  "              name: config\n"\
  "          securityContext:\n"\
  "            privileged: true\n"\
  "      volumes:\n"\
  "        - name: dev-snd\n"\
  "          hostPath:\n"\
  "            path: /dev/snd\n"\
  "        - name: dev-shm\n"\
  "          hostPath:\n"\
  "            path: /dev/shm\n"\
  "        - name: config\n"\
  "          hostPath:\n"\
  "            path: /mnt/reorchestrator/jitsi-data/jibri-var/config\n"\
  "        - name: prosody-script\n"\
  "          hostPath:\n"\
  "            path: /mnt/reorchestrator/jitsi-data/prosody-var/scriptss\n"\
  "        - name: web-config\n"\
  "          hostPath:\n"\
  "            path: /mnt/reorchestrator/jitsi-data/web-var/config\n"\
  "        - name: web-images\n"\
  "          hostPath:\n"\
  "            path: /mnt/reorchestrator/jitsi-data/web-var/images\n"\
  "---\n"\
  "apiVersion: v1\n"\
  "kind: Service\n"\
  "metadata:\n"\
  "  labels:\n"\
  "    service: "+str(jvbServiceName)+"\n"\
  "  name: "+str(jvbServiceName)+"\n"\
  "  namespace: jitsi\n"\
  "spec:\n"\
  "  type: NodePort\n"\
  "  externalTrafficPolicy: Cluster\n"\
  "  ports:\n"\
  "  - port: "+jvbServicePort+"\n"\
  "    protocol: UDP\n"\
  "    targetPort: "+jvbServicePort+"\n"\
  "    nodePort: "+jvbServicePort+"\n"\
  "  selector:\n"\
  "    k8s-app: "+k8sapp+"\n"\
  "---\n"\
  "apiVersion: v1\n"\
  "kind: Service\n"\
  "metadata:\n"\
  "  labels:\n"\
  "    service: "+webServiceName+"\n"\
  "  name: "+webServiceName+"\n"\
  "  namespace: jitsi\n"\
  "spec:\n"\
  "  ports:\n"\
  "  - name: 'https'\n"\
  "    port: 443\n"\
  "    targetPort: 443\n"\
  "    nodePort: "+str(webServicePort)+"\n"\
  "  type: NodePort\n"\
  "  selector:\n"\
  "    k8s-app: "+k8sapp+"\n"

  dosya.write(satir1)  # yazdirma islemi
  dosya.close()

minDesiredDep = 5 #olmasi istenen en az deployment sayisi
maxConferenceOneDeployment = 5 # bir jvd de maksimum konferans sayisi

webPortStart = 30211
maxConfernceNumber = 200
webportEnd = webPortStart + maxConfernceNumber - 1 

time_diff = 7200


session_ids = list()
session_web_ports = list()
session_loads = list()
create_times = list()


def apply_et(dosya_adi):
  log_ekle( str( os.system("kubectl apply -f "+dosya_adi) ) )

def delete_et(dosya_adi):
  log_ekle( str( os.system("kubectl delete -f "+dosya_adi) ) )

def deploy_et(bos_port, record_id):
  dosya_olustur(bos_port, record_id)
  apply_et("orch-deployment.yml")

  log_ekle(str(bos_port) + " web portu ile jitsi deploy edildi.Dep. Name:jitsi-jibri-"+str(bos_port))

def deploy_sil(silinecek_deployment_web_port_number):
  dosya_olustur(silinecek_deployment_web_port_number,"orch-deployment.yml")
  delete_et("orch-deployment.yml")

  log_ekle(str(silinecek_deployment_web_port_number) + " web portu ile jitsi delete edildi.Dep. Name:jitsi-"+str(silinecek_deployment_web_port_number))

  db = Database()
  db.insert("delete from sessions_jibri where session_web_port='"+str(silinecek_deployment_web_port_number)+"'")
  db.close()

def main():
  
  db = Database()
  cursor = db.select("select session_id, session_web_port, create_time from sessions_jibri")

  session_ids = []
  session_web_ports = []
  create_times = []

  for (session_id, session_web_port, create_time) in cursor:
    session_ids.append(session_id)
    session_web_ports.append(int(session_web_port))
    time = "{:%s}".format(create_time)
    create_times.append(time)

  

  for i in range(webPortStart, webportEnd):
    if i not in session_web_ports:
      bos_port = i
      break

  row_id = db.insert("insert into sessions_jibri (session_web_port,session_uniq_id) VALUES('"+str(bos_port)+"','"+str(args[2])+"')")
  db.insert("insert into sessions_logs (session_web_port,session_uniq_id) VALUES('"+str(bos_port)+"','"+str(args[2])+"')") 
  db.close()

  deploy_et(bos_port, str(args[2]))
  print(bos_port)
  return bos_port


def main2():
  deploy_sil(args[2])

def main3():
  db = Database()
  cursor = db.select("select record_path from video_records where record_id="+str(args[2]))
  rec_ids = list()
  for record_path in cursor:
    rec_ids.append(record_path)
  a = db.insert("delete from video_records where record_id="+str(args[2]))
  db.close()
  path = rec_ids[0][0]
  paths = path.split("/")
  if len(paths[0]) > 0 :
    stra ="rm -r /mnt/reorchestrator/jitsi-data/jibri-var/config/recordings/"+paths[0]
    os.system(stra)
  else:
    return "Silme basarisiz. Kayit bulunamadi."
  return "Silme basarili."



def cleaner():
  
    db = Database()
    cursor = db.select("select session_id, session_web_port, create_time from sessions_jibri")

    session_ids = []
    session_web_ports = []
    create_times = []
    session_cpu_loads = []
    for (session_id, session_web_port, create_time) in cursor:
        session_ids.append(session_id)
        session_web_ports.append(int(session_web_port))
        time = "{:%s}".format(create_time)
        create_times.append(time)

    for port in session_web_ports:
      result = subprocess.run(['./get_cpu.sh', str(port)], stdout=subprocess.PIPE)
      res = str(result.stdout.decode('utf-8'))
      session_cpu_loads.append(str(res[0:len(res)-2]))
  
    for i in range(len(create_times)):
      time = create_times[i]
      now = "{:%s}".format(datetime.datetime.now())
      now = int(now) + 10800
      if(int(now) - int(time) > 900): # olusturulduktan 15 dakika gecityse
        if(int(session_cpu_loads[i]) < 30 ): # ve node uzerinde islem yoksa
          deploy_sil(session_web_ports[i])  #deploymenti sil
      if(int(now) - int(time) > 21600): #6 saattir hala aciksa
        deploy_sil(session_web_ports[i])


if args[1]=="create":
  main()
elif args[1]=="destroy":
  main2()
elif args[1]=="delete_video_record":
  print(main3())
elif args[1]=="cleaner":
  while True:
    cleaner()
    time.sleep(60)

else :
  print("Error! Page not found.")
