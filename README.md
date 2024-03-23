# Описание

Скрипт который берет два списка контактов (предполагется [Brandmeister](https://brandmeister.network) и [QRA-TEAM](https://qra-team.ru)) в виде csv-файлов ищет там совпадения, объединяет информацию о позывных в одно поле и складывает в третий файл подходящий для радиостанции с [OpenGD77](https://www.opengd77.com/) прошивкой

# Как пользоваться

Под linux либо под Windows в [WSL](https://learn.microsoft.com/ru-ru/windows/wsl/install)

## Непосредственно python script

```
python3 merger.py qra-hams.csv bm-hams.csv user.csv
```

можно передавать заголовок для csv

```
python3 merger.py qra-hams.csv bm-hams.csv user.csv CALLSIGN,RADIO_ID,FIRST_NAME,CITY,STATE,COUNTRY
```

можно еще фильтровать записи по префиксу dmrId

```
python3 merger.py qra-hams.csv bm-hams.csv user.csv CALLSIGN,RADIO_ID,FIRST_NAME,CITY,STATE,COUNTRY 250
```

тогда на выходе будут контакты BM из России (с префиксом 250) + QRA-TEAM

## С помощью заготовленного [скрипта](run.sh)

```
bash run.sh
```

этот скрипт качает контакты отсюда

https://radioid.net/static/user.csv

https://raw.githubusercontent.com/krot4u/Public_scripts/master/dmrid.dat

и запускает Python скрипт выше на выхлопе получается файл подходящий для OpenGD77

есть еще второй [скрипт](run-rt73.sh)

```
bash run-rt73.sh
```

делает тоже самое на подает на вход другой формат

```
python3 merger.py qra-hams.csv bm-hams.csv user.csv CALLSIGN,RADIO_ID,FIRST_NAME,CITY,STATE,COUNTRY 250
```

на выхлопе получается файл подходящий для [Retevis RT73](https://www.radioscanner.ru/forum/topic51444.html) он же [Kydera CDR-300UV](https://kydera.su/dmr-radiostancii/kydera-cdr-300uv-dmr-analog-radio)

# Результат

Выхлоп получается вида

```
2504024,R4AAAN/URAL,Vitaly,Korol,Volgograd,All Regions,Russia
2504025,R4WBN,,,,,Russia
2504026,R4ACZ,,,,,Russia
2504027,UA4CTO,Vyacheslav,,,,Russia
2504028,R4HGC/SHAPRAN,Aleksander,,,,Russia
2504029,RW4CFA,,,,,Russia
2504030,R4KK/BOEC,Sergey,,,,Russia
2504031,UB4WBS/ENGENR,Andrey,Mokhov,Krasnogorsk,,Russia
```

# Дисклеймер

Проверялось на [Retevis RT3S](https://www.ixbt.com/live/gadgets/cifroanalogovaya-dmr-radiostanciya-retevis-rt3s-s-gps-i-vozmozhnostyu-zapisi-peregovorov.html) с прошивкой [OpenGD77](https://www.opengd77.com/)