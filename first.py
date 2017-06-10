print "hi again"

try:
    zip_code = int(raw_input("enter zip"))
    print zip_code

except ValueError, err_obj:
    print err_obj

print 'next stmt after exception'
