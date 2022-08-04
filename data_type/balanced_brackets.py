n = int(input())
balanced = 0
for i in range(1, n + 1):
    next_symbol = input()
    if next_symbol == "(":
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
    elif next_symbol == ")":
        balanced -= 1
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
