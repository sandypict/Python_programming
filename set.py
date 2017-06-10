
item=set()

print item
print type(item)
print len(item)

item=set(['pam',12,21,123,'eva'])

item.add('emc')
value=item.pop()

print value
print item

item.remove(12)

for i in item:
    print i



#Dictionary ,,, set and list comprehension




# Set is always unique. When  assigned a list with duplicate values to set, it will remove duplicate entries