items=[1111,22,3,4]
items.sort()
print items
items.sort(reverse=True)
print items

s=sorted(items)
print s
print
print items

for index, item in enumerate(items):
    print index, '->', item

