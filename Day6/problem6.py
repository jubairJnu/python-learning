#  integer value reverse print

a = int(input("Enter number"))

rev_a = 0

while a>0:
    last_value = a%10
    rev_a = rev_a*10 + last_value
    a//=10
print(rev_a)