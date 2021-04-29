#!/bin/sh
sleep 5
mkdir /etc/prosody
cp -r /config/* /etc/prosody
sleep 5
/usr/bin/prosodyctl register $H_NAME $XMPP_DOMAIN $H_PASSW
echo $H_NAME ile $H_PASSW  ve $XMPP_DOMAIN kullanilarak prosody kullanici olusturuldu.
sleep infinity
