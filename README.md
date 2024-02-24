# Описание

Скрипт который берет два списка контактов (предполагется Brandmeister и QRA-TEAM) в виде csv-файлов ищет там совпадения, объединяет информацию о позывных в одно поле и складывает в третий файл.

# Как пользоваться

Под linux либо под Windows в WSL

## Непосредственно python script

```
python3 merger.py qra-hams.csv bm-hams.csv out.csv
```

можно еще фильтровать записи по локации

```
python3 merger.py qra-hams.csv bm-hams.csv out.csv Kazakhstan
```

тогда на выходе будут контакты BM из Казахстана + QRA-TEAM

## С помощью заготовленного скрипта

```
sh run.sh
```

этот скрипт качает контакты отсюда

http://kavkaz.qrz.ru/dmrid_rus.csv

https://qra-team.online/files/Kydera880uv_Contact.csv

Обрезает в Kydera файле первую строчку и удаляет кавычки

```
tail -n +2 tmp.csv | sed 's/""""//g' > qra-hams.csv
```

и запускает Python скрипт выше

# Выхлоп получается вида

```
2485248,UB3ZZZZ (Vasyan),Vasily,,,Russia Fed
2485249,UB3YYYY (Petyan),Petyan,,,Russia Fed
2485250,UB3XXXX (Kostyan),Kostyan,,,Russia Fed
```