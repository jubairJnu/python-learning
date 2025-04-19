# from the given list which number frequecny i greater than k

a = [1,2,3,3,4,3,5,3,4,5,4,6,4,5,6,7,4,5,6]

res = []
k = 3

for i in a:
    freq = a.count(i)
    if freq > k and i not in res:
        res.append(i)

print(res)