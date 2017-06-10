import math

try:
    num=int(raw_input("Enter number"))
    fmt="{:>4}"
    print fmt.format('*'),
    i=1
    while i <= num:
        print fmt.format(i)
        for j in range(1,num+1):
            print fmt.format(i*j),
        i = i+1
except ValueError, err_obj:
    print err_obj