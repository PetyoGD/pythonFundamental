word_string = [s for s in input().split()]
word = [w for w in word_string if len(w) % 2 == 0]
print("\n".join(word))
