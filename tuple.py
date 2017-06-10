
items=('andy', 'sandeep')

# This is perfectly correct if we skip brackets below. It will create tuple
tuple1 = 1,2,3


print tuple1

# This is willl create a scalar but not single element tuple
n=(1000)
print n

# To do this
n=(1000,)
print n

n=1000,
print n

#Applications of tuple

#1. Parallel Assignment
name,age = t= 'sandeep', 33
print t
print name
print age

#2. To returm more than one value from a function

q,r = divmod(5.0,2) # divmod returns a tuple
print q
print r

def sqr_n_cube(value):
    return value**2, value**3

print sqr_n_cube(5)
