from timeit import timeit

def demo1():
    items=[1,2,3,4]
    temp=list()

    for i in items:
        temp.append(bin(i))
    return temp

def demo2():
    items = [1, 2, 3, 4]
    return [bin(item) for item in items]

print timeit('demo1()',setup='from __main__ import demo1')
print timeit('demo2()',setup='from __main__ import demo2')

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print [row for row in mat]

print [row[1] for row in mat]

#Matrix Transpose
print [[row[i] for row in mat] for i in [0,1,2]]

#nested loop. In a way it flattens a list of lists
print [col for row in mat for col in row]

print [col for row in mat for col in row if col%2]

mat = [[1,2,3],
       [4,5,6,10],
       [7,8,9]]
print [col for row in mat if len(row)==3 for col in row if col%2]