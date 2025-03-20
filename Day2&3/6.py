#  logical operator

# and

print("and true", 10-4 == 6 and 16+4 ==20);
print("and false", 10-4 == 6 and 16+4 ==24);

# or

print("Or true", 10-4 == 6 and 16+4 ==29);
print("Or false", 10-4 == 16 and 16+4 ==24);

# not 

print(not(10+4 == 14))

# if else elif

marks = 9

if( marks>= 90 and marks<=100 ):
    print("Tumi Valo And 2 ta price paba");
elif(marks>=80 and marks<90):
    print("Average and 1 ta price");
else:
    print("dure giye mor");