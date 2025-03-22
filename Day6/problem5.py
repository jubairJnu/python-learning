#  check if the given number is armstrong

a= int(input("enter a number"))

num_lent = len(str(a));

temp = a
sum =0

while temp>0:
    last_digit = temp%10
    sum = sum + last_digit**num_lent
    temp //=10

if sum == a:
    print("Armstrong")
else:
    print("Not Armstrong")
