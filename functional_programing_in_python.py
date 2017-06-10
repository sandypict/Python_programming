
# This is how we do FUNCTIONAL PROGRAMMING in python.
# A function bin, is passed as an argument to another (map)
items=[1,2,3,4]
temp2=map(bin, items)

print temp2


s='this is a simple string'
items=s.split()
print items
print map(str.upper, items)
