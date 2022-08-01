first_string = input()
second_string = input()
# last_version = first_string
# for index in range(len(second_string)):
#     left_part = second_string[:index + 1]
#     right_part = first_string[index + 1:]
#     current_string = left_part + right_part
#     if current_string == last_version:
#         continue
#     print(current_string)
#     last_version = current_string
last_version = first_string
for symbol in range(len(first_string)):
    new_string = ""
    for beginning in range(0, symbol + 1):
        new_string += second_string[beginning]
    for ending in range(symbol + 1, len(first_string)):
        new_string += first_string[ending]
    if new_string == last_version:
        continue
    print(new_string)
    last_version = new_string
