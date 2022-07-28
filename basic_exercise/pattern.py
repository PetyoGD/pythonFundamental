number = int(input())
index = 0
for column in range(number+1):
    for row in range(1,column+1):
        print("*",end="")
    print()
for column in range(number -1, 0, -1):
    for row in range(1, column+1):
        print("*", end="")
    print()
