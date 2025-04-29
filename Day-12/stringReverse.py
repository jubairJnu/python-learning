a = input("Enter :")
a = a.split()

result = ""

for i in a :
    result +=  i[::-1] + " "
print(result)