import wimedb
import sys
from subprocess import call

database = sys.argv[1]

for i in range(2, len(sys.argv)):
    wimedb.remove(sys.argv[i], database)
    call(["rm", "-rf", sys.argv[i]])
