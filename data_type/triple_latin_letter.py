numbers = int(input())

for i in range(numbers):
    for j in range(numbers):
        for k in range(numbers):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
