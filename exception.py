#exec_inf

from sys import exec_info
from traceback import print_tb
try:
    print "Hi"

except:
    print exec_info()
    print_tb((exec_info()[2]))

