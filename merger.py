#!/usr/bin/env python3

import csv
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
fileOut = sys.argv[3]

prefix = ""

if len(sys.argv) > 4:
    prefix = sys.argv[4]
    print(f"prefix {prefix}")

file1data = {}

print(f"reading first file: {file1}")
with open(file1, "r", newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter=',')
    for row in rdr:
        data = {}
        data['id'] = row[1]
        data['callsign'] = row[0]
        file1data[row[1]] = data

print(f"total members in {file1}: {len(file1data)}")
print(f"reading second file: {file2}")

with open(file2, "r", newline='') as csvfile:
    with open(fileOut, "w", newline='') as outfile:
        rdr = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(["RADIO_ID","CALLSIGN","FIRST_NAME","LAST_NAME","CITY","STATE","COUNTRY"])
        for row in rdr:
            if len(prefix) > 0 and not row[0].startswith(prefix):
                continue

            id = row[0]
            callsign = row[1]
            fname = row[2]
            lname = row[3]
            city = row[4]
            state = row[5]
            country = row[6]

            if id in file1data:
                print(f"match found {row} / {file1data[id]}")
                row1 = [id, f"{callsign}/{file1data[id]['callsign']}", fname, lname, city, state, country]
                writer.writerow(row1)
                file1data.pop(row[0])
            else:
               writer.writerow(row)

        print(f"{file1} members left unmatched: {len(file1data)} adding them as is")
        for _, el in file1data.items():
            row1 = [el['id'], el["callsign"], '', '', '', '', 'Russia']
            writer.writerow(row1)