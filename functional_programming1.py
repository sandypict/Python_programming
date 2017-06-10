from pprint import pprint as pp

ascii = [112, 110, 109]

def tag_it(av):
    return 'asciiiiii{}--{}'.format(chr(av),av)

pp(map(tag_it, ascii))

# by using lambda

pp(map(lambda av: 'ascii***iiii{}--{}'.format(chr(av),av),  ascii))

items=range(1,154)

print map(lambda n: n%7==0, items)
# Observer the behavior of filter below. It filters out output.
print filter(lambda n: n%7==0, items)

import re
pattern="^root"

for line in filter(lambda line: re.search(pattern, line), open('c:\password.txt')):
    print line

## github.com/ravijaya/python-documents
#ravi.goglobium@gmail.com
#97909 16181
