
from sys import argv
print argv

def power (x,n=0):
    return x*n

print power(4,2)
print power(4,4)
print power(4)
'''
def file_copy_mirrir(source=NA, dest=NA):
    if source==NA or dest==NA:
        print "Insufficinet arguments""
        return
    else:
        for line in open(source):
'''
# function accepting Variable length argument
def demo(*args):
    print args

demo()
demo(123)
demo(1,2,3)
items=(1,2,3,4)

# Following will pass a tuple of a list
demo(items)

# Following will pass content of the list
demo(*items)

def compute(a,b,c):
    print a+b+c
items1=[1,2,3,4]

compute(items1[0],items1[1],items1[2])
compute(*items1[-3:])

