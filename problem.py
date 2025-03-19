# problem 1

length = int(input("enter length"))
breath = int(input("enter breath"))

if(length == breath):
    print("it is square");
else:
    print("not square");

# problem 2

input_1 = int(input("enter 1st"))
input_2 = int(input("enter 2st"))
input_3 = int(input("enter 3st"))

if(input_1 < input_2 and input_2 < input_3):
    print("input 1 is larger", input_1);
elif(input_2< input_3):
    print("Input 2 is large", input_2);
else:
    print("input 3 is large", input_3);

# # problem 3

# number = 12
# if(number%2 == 0):
#     print("Number is enven");
# else:
#     print("Nubmer is odd");

# # problem 4

marks = int(input("enter marks:"))

if(marks>90):
    print("Your grage A");
elif(marks>80 and marks<=90):
    print("B");
elif(marks>=60 and marks<=80):
    print("C");
else:
    print("D");

# # problem 5

year = 1997
if((year % 400 ==0 and year%100 ==0) or (year%4 ==0 and year% 100 != 0 ) ):
    print("Leap year");
else:
    print("Not Leap Year");

