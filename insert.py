import wimedb
import sys

database = sys.argv[1]

for i in range(2, len(sys.argv)):
    wimedb.insert(sys.argv[i], database)
