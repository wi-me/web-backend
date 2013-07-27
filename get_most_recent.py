import wimedb
import json
import sys

database = sys.argv[1]
output = sys.argv[2]

row = wimedb.get_most_recent(database)

json_dict = {}
json_dict["NAME"] = row[1].encode('ascii', 'ignore')
json_dict["ARTIST"] = row[2].encode('ascii', 'ignore')

json_str = json.dumps(json_dict)

file = open(output,'w')
file.write(json_str)
