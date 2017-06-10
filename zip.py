
# Parallel iteration
names=['a','b','c']
ages=[1,2,3]

print zip(names,ages)

for n,a in zip(names,ages):
    print "{:>16} {:>5}".format(n,a)