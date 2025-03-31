matrix =[[1,2],[3,4],[5,6]]


a =[]

for row in range(2):  # outer function
    b = []
    for col in matrix:  # innner function
        b.append(col[row])
    a.append(b)
print(a)

# in list comprehesion

res = [[col[row] for col in matrix] for row in range(2)]
print(res,"rs")