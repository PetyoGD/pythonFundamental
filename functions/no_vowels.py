rand_string = input()
rand_string_list = [m for m in rand_string]
vowel_list = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
removing_str = [x for x in rand_string_list if x not in vowel_list]
print("".join(removing_str))

# rand_string = input()
# vowel_list = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
# removing_str = [x for x in rand_string if x not in vowel_list]
# print("".join(removing_str))
