## Installation and explanation

It is **assumed** that docker and kubernetes **installed** and working.

All steps must be run on the **master node.**



Clone the repository:

```bash
$ git clone https://github.com/muazdervent/jitsi-re0rchestrator-api.git
```

Set the envr.sh(you can give the value you want, these will be used for setup ):
```bash
$ cd jitsi-re0chestrator-api
$ nano envr.sh
```

Run the setup.sh(only enter for npm entries towards the end):
```bash
./setup.sh
```

After the setup.sh:

1)Make sure your mysql deployment is running.

```bash
$ kubectl get pods
```
2)Run this commands:
```bash
$ cd express
$ python3 create_tables.py
$ forever start express.js
$ nohup ./cleaner.sh &
```
3)Make sure that express.js and cleaner.sh are constantly running in the background. 
