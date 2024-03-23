# Описание

Скрипт который берет два списка контактов (предполагется [Brandmeister](https://brandmeister.network) и [QRA-TEAM](https://qra-team.ru)) в виде csv-файлов ищет там совпадения, объединяет информацию о позывных в одно поле и складывает в третий файл подходящий для радиостанции с [OpenGD77](https://www.opengd77.com/) прошивкой

# Как пользоваться

Под linux либо под Windows в [WSL](https://learn.microsoft.com/ru-ru/windows/wsl/install)

## Непосредственно python script

```
python3 merger.py qra-hams.csv bm-hams.csv out.csv
```

можно еще фильтровать записи по префиксу dmrId

```
python3 merger.py qra-hams.csv bm-hams.csv out.csv 250
```

тогда на выходе будут контакты BM из России (с префиксом 250) + QRA-TEAM

## С помощью заготовленного скрипта

```
sh run.sh
```

этот скрипт качает контакты отсюда

https://radioid.net/static/user.csv

https://raw.githubusercontent.com/krot4u/Public_scripts/master/dmrid.dat

и запускает Python скрипт выше

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