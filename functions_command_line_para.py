
## run as c:\Python27\python.exe functions_command_line_para.py c:\password.txt c:\temp.txt

from sys import argv

def usage():
    print "usage"
    exit(1)

def mirrir_copy(src_file, dest_file):
    with open(src_file) as fp, open(dest_file, 'w') as fw:
        for line in fp:
            reversed_line= line.rstrip()[::-1]
            fw.write(reversed_line + '\n')

if len(argv)!=3:
    usage()

mirrir_copy(argv[1], argv[2])

