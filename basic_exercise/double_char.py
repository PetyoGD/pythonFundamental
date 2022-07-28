word = input()
while word != "End":
    for char in word:
        print(char * 2, end="")
    print()
    word = input()
