from pprint import pprint as pp

list1=[]
dict1={}
with open('C:/textfile.txt','r') as fp:
    for line in fp:
        list1.append(line.split())


list2 = [col for row in list1 for col in row]
print list2


for i in list2:
    if i in dict1:
        dict1[i]= dict1[i] + 1
    else:
        dict1[i]=1

print dict1.items()
