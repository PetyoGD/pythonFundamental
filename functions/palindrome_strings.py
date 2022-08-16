random_str = input().split()
palindrome = input()
palindrome_list = []
palindrome_count = 0
for word in random_str:
    if word == "".join(reversed(word)):
        palindrome_list.append(word)
for same in random_str:
    if same == palindrome:
        palindrome_count += 1
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")
