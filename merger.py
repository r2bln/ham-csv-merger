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

csvHeader = "RADIO_ID,CALLSIGN,FIRST_NAME,LAST_NAME,CITY,STATE,COUNTRY"
csvFormat = csvHeader.split(",")

def printRow(writer, data):
    rowOut = []
    for key in csvFormat:
        if key in data:
            rowOut.append(data[key])
        else:
            rowOut.append('')
    writer.writerow(rowOut)

def main():
    file1data = {}

    print(f"reading first file: {file1}")
    with open(file1, "r", newline='') as csvfile:
        rdr = csv.reader(csvfile, delimiter=';')
        for row in rdr:
            data = {}
            data['RADIO_ID'] = row[0]
            data['CALLSIGN'] = row[1]
            data['COUNTRY'] = 'Russia'
            file1data[row[0]] = data

    print(f"total members in {file1}: {len(file1data)}")
    print(f"reading second file: {file2}")

    with open(file2, "r", newline='') as csvfile:
        with open(fileOut, "w", newline='') as outfile:
            rdr = csv.DictReader(csvfile, delimiter=',')
            writer = csv.writer(outfile, delimiter=',')
            writer.writerow(csvFormat)
            for row in rdr:
                id = row['RADIO_ID']

                if len(dmrIdPrefix) > 0 and not id.startswith(dmrIdPrefix):
                    continue

                if id in file1data:
                    print(f"match found {row} <<->> {file1data[id]}")
                    row["CALLSIGN"] = f"{row['CALLSIGN']}/{file1data[id]['CALLSIGN']}"
                    file1data.pop(row["RADIO_ID"])

                printRow(writer, row)

            print(f"{file1} members left unmatched: {len(file1data)} adding them as is")
            for _, el in file1data.items():
                printRow(writer, el)
 
if __name__ == "__main__":
    main()