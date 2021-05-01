#!/bin/bash
. ./envr.sh

echo -e "#!/bin/bash    \n"\
"RECORDINGS_DIR=\$1  \n"\
"arrIN=(\${RECORDINGS_DIR//// })  \n"\
"last=""  \n"\
"last=\${arrIN[-1]}  \n"\
"arrIN=(\${lastt//// })  \n"\
"video=\$(find \$RECORDINGS_DIR -print | grep -i .mp4)  \n"\
"arrN=(\${video//// })  \n"\
"video=\${arrN[-1]}  \n"\
"x=\$last/\$video  \n"\
"if [ \"\$VERSION\" == \"canli\" ]; then  \n"\
"   db=\"video_record\";  \n"\
"   ses=\"session_uniq_name\"  \n"\
"else  \n"\
"   db=\"video_records\";  \n"\
"   ses=\"session_uniq_id\"  \n"\
"fi  \n"\
"mysql -h "$mysql_ip" -P "$mysql_port" -uroot -p'"$mysql_password"' "$mysql_database"<<EOFMYSQL  \n"\
"insert into \$db (\$ses,record_path) values('\$SESSION_UNIQ_ID','\$x');  \n"\
"  \n"\
"  \n"\
" \n" > ./jitsi-data/jibri-var/config/finalize1.sh
