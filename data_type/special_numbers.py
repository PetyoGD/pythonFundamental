n = int(input())
for i in range(1, n + 1):
    sum_digit = 0
    digit = i
    while digit > 0:
        sum_digit += digit % 10
        digit = digit // 10
    if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
