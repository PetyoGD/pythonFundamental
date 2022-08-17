list_input = input().split(", ")
even_list = []
number_list = list(map(lambda x: int(x), list_input))
for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        even_list.append(i)
print(even_list)
