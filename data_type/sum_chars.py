numbers = int(input())
sum_chars = 0
for i in range(numbers):
    next_char = input()
    sum_chars += ord(next_char)
print(f"The sum equals: {sum_chars}")
