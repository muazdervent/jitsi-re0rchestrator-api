#!/bin/bash
    RECORDINGS_DIR=$1
    #echo "This is a dummy finalize script" > /tmp/finalize.out
    #echo "The script was invoked with recordings directory $RECORDINGS_DIR." >> /tmp/finalize.out
    #echo "You should put any finalize logic (renaming, uploading to a service" >> /tmp/finalize.out
    #echo "or storage provider, etc.) in this script" >> /tmp/finalize.out
    #exit 0
arrIN=(${RECORDINGS_DIR//// })  #split /
last=""
last=${arrIN[-1]}



arrIN=(${lastt//// })
video=$(find $RECORDINGS_DIR -print | grep -i .mp4)

arrN=(${video//// })
video=${arrN[-1]}
x=$last/$video





if [ "$VERSION" == "canli" ]; then
   	db="video_record";
	ses="session_uniq_name"
else
	db="video_records";
	ses="session_uniq_id"
fi


mysql -h YOUR_MYSQL_SERVER_IP -P YOUR_PORT -uroot -p'YOUR_PASSWOR' reorchestrator<<EOFMYSQL
insert into $db ($ses,record_path) values('$SESSION_UNIQ_ID','$x');

EOFMYSQL
