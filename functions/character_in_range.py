def series_in_ascii(a, b):
    a = ord(a)
    b = ord(b)
    list_chars = []
    for digit in range(a+1,b):
        list_chars.append(chr(digit))
    return list_chars


first_num = input()
second_num = input()
print(" ".join(series_in_ascii(first_num,second_num)))
