#!/bin/sh

rm -rf *.csv
wget https://radioid.net/static/user.csv -O bm-hams.csv
wget https://raw.githubusercontent.com/krot4u/Public_scripts/master/dmrid.dat -O qra-hams.csv
python3 merger.py qra-hams.csv bm-hams.csv user.csv 250