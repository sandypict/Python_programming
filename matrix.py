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

