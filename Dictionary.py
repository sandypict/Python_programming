info={
    'host':'ws1',
    'domain':'emc.com'
}

print info
item='version'
if item not in  info:
    info[item]=3.4
print info

#deleting a key

value=info.pop('domain')
# or del info['domain']
print info

print info['host']
print info.get('host')
print info.get('invalid_key')
print info.get('invalid_key','invalid_key')

print info.keys()
print info.values()
print info.items()

for item in info:
    print item, '->', info[item]

for k,v in info.iteritems():
    print k, '->', v