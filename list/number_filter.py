num = int(input())
collections_digits = []
even_list = []
odd_list = []
negative_list = []
positive_list = []
for i in range(num):
    digit = int(input())
    if digit % 2 == 0:
        even_list.append(digit)
    if digit % 2 != 0:
        odd_list.append(digit)
    if digit >= 0:
        positive_list.append(digit)
    if digit < 0:
        negative_list.append(digit)
operation = input()
if operation == "even":
    print(even_list)
elif operation == "odd":
    print(odd_list)
elif operation == "positive":
    print(positive_list)
else:
    print(negative_list)
