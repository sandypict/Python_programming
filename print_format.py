from math import pi

#Sting formatting
#{:fmt_str}


area= 3.11444444
radius = 1
print 'radius : {}\narea : {:.3f}'.format(radius, area)

name,age,gender = 'sarah',4,'female'

print "|{}|{}|{}|".format(name,age,gender)
print "|{:22}|{:9}|{:22}|".format(name,age,gender)
print "|{}|{}|{}|".format(name,age,gender)
print "|{}|{}|{}|".format(name,age,gender)

