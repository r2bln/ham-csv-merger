#!/bin/sh

rm -rf *.csv
wget http://kavkaz.qrz.ru/dmrid_rus.csv -O bm-hams.csv
wget https://s3.qra-team.online/Devices_Contact_List/Kydera880uv_Contact.csv -O tmp.csv
tail -n +2 tmp.csv | sed 's/""""//g' > qra-hams.csv
rm tmp.csv
python3 merger.py qra-hams.csv bm-hams.csv out.csv