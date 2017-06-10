from pprint import pprint as pp
with open('C:/password.txt','r') as fp:
    for line in fp:
        line.split(':')
        #print sorted(line.split(':')[0:1])

#Using list comprehension

ul=[line.split(':')[0].upper() for line in open('c:/password.txt') if line.startswith('a')]

for line_no, user in enumerate(sorted(ul),1):
    print line_no,'',user
    #pp(sorted(ul))

# following will return list of lists
content=[line.rstrip().split(':') for line in open('c:/password.txt')]
pp(content)

for user_info in content:
    print "{}:{}:{}".format(user_info[2],user_info[0],user_info[-1])