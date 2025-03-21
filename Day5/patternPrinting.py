# for row in range(3):
#     for col in range(row +1):
#         print("#", end="")
#     print()


for row in range(6):
    for col in range(row+1):
        print(chr(97+row),end=" ")
    print()