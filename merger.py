#!/usr/bin/env python3

import csv
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
fileOut = sys.argv[3]

dmrIdPrefix = ""

if len(sys.argv) > 4:
    dmrIdPrefix = sys.argv[4]
    print(f"dmrIdPrefix {dmrIdPrefix}")

file1data = {}

print(f"reading first file: {file1}")
with open(file1, "r", newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter=';')
    for row in rdr:
        data = {}
        data['id'] = row[0]
        data['callsign'] = row[1]
        file1data[row[0]] = data

print(f"total members in {file1}: {len(file1data)}")
print(f"reading second file: {file2}")

with open(file2, "r", newline='') as csvfile:
    with open(fileOut, "w", newline='') as outfile:
        rdr = csv.DictReader(csvfile, delimiter=',')
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(["RADIO_ID","CALLSIGN","FIRST_NAME","LAST_NAME","CITY","STATE","COUNTRY"])
        for row in rdr:
            if len(dmrIdPrefix) > 0 and not row['RADIO_ID'].startswith(dmrIdPrefix):
                continue

            id = row["RADIO_ID"]
            callsign = row["CALLSIGN"]
            fname = row["FIRST_NAME"]
            lname = row["LAST_NAME"]
            city = row["CITY"]
            state = row["STATE"]
            country = row["COUNTRY"]

            if id in file1data:
                print(f"match found {row} <<->> {file1data[id]}")
                row1 = [id, f"{callsign}/{file1data[id]['callsign']}", fname, lname, city, state, country]
                writer.writerow(row1)
                file1data.pop(row["RADIO_ID"])
            else:
               writer.writerow(row.values())

        print(f"{file1} members left unmatched: {len(file1data)} adding them as is")
        for _, el in file1data.items():
            row1 = [el['id'], el["callsign"], '', '', '', '', 'Russia']
            writer.writerow(row1)