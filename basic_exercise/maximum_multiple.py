import sys

divisor = int(input())
boundary = int(input())
max_digit = -sys.maxsize
for digit in range(divisor, boundary + 1):
    if digit % divisor == 0:
        if max_digit < digit:
            max_digit = digit
print(max_digit)
