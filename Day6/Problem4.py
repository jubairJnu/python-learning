#  give count of number 

#  Method 1 : long cut 

a = int(input("enter some numbers"));

count = 0;
while a>0:
    digit = a%10 # for get last digit
    # print("digit", digit) getting last digit
    count = count+1
    a =  a // 10
    print(count,"count")

# Method 2 short cut

b= input("enter:")

print(len(b))
