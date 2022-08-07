n = int(input())
search_str = input()
gathered_str = []
selected_str = []
for i in range(n):
    loaded_str = input()
    gathered_str.append(loaded_str)
    if search_str in loaded_str:
        selected_str.append(loaded_str)
print(gathered_str)
print(selected_str)
