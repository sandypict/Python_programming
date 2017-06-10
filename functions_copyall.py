# Run as
#\Users\chavas5\PycharmProjects\untitled>c:\Python27\python.exe functions_copyall.py a.txt b.txt c.txt

from sys import argv

def copy_all(*args):
    with open(args[-1],'w') as fw:
        for file_name in args[:-1]:
            fw.write(file_name.center(60,'-')+'\n')
            fw.write(open(file_name).read())
            fw.write('-'.center(60,'-')+'\n')

copy_all(*argv[1:])
