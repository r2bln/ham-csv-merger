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
        data['id'] = row[0]
        data['callsign'] = row[1]
        data['name'] = row[2]
        data['loc'] = row[5]
        file1data[row[0]] = data

print(f"total members in {file1}: {len(file1data)}")
print(f"reading second file: {file2}")

with open(file2, "r", newline='') as csvfile:
    with open(fileOut, "w", newline='') as outfile:
        rdr = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(outfile, delimiter=',')
        for row in rdr:
            if len(prefix) > 0 and not row[5].startswith(prefix):
                continue

            id = row[0]
            callsign = row[1]
            name = row[2]

            if id in file1data:
                print(f"match found {row} / {file1data[id]}")
                row1 = [id, f"{callsign} ({file1data[id]['callsign']})", name, "" , "", file1data[id]["loc"]]
                writer.writerow(row1)
                file1data.pop(row[0])
            else:
               writer.writerow(row)

        print(f"{file1} members left unmatched: {len(file1data)} adding them as is")
        for _, el in file1data.items():
            row1 = [el["id"], el["callsign"], el["name"], "" , "", el["loc"]]
            writer.writerow(row1)