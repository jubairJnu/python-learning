#  fibonacci

a,b = 0,1;

for i in range(10):
    print(a, end=" ")
    result = a+b
    a = b
    b= result