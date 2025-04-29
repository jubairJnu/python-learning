a = input("Enter")
res = ""

for i in range(0,len(a),2):
    res = res + a[i]*int(a[i+1])
result = sorted(res,key=str.casefold)
res_string = "".join(result)

print(res_string)