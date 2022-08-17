first_series = input().split(", ")
second_series = input().split(", ")
word_in = []
for first_word in first_series:
    for second_word in second_series:
        if first_word in second_word and not first_word in word_in:
            word_in.append(first_word)
print(word_in)