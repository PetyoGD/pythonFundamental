list_words = [s for s in input().split()]
decoded = []
for letter in list_words:
    digit = [s for s in letter if s.isdigit()]
    rest = [s for s in letter if s not in digit]

    digit_letter = chr(int("".join(digit)))
    rest[0], rest[-1] = rest[-1], rest[0]
    whole_word = digit_letter + "".join(rest)
    decoded.append(whole_word)
print(" ".join(decoded))

