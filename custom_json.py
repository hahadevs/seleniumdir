import csv
import json

csvfile = open('csvdir/redfin.csv', 'r')
jsonfile = open('jsondir/redfin.json', 'w')

fieldnames = ("","url","price","location","amenities")
reader = csv.DictReader( csvfile, fieldnames)
json_dict = []
for row in reader:
    json_dict.append(row)

jsonfile.write(json.dumps(json_dict))