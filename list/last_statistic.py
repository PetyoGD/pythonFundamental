num = int(input())
positive = []
negative = []
for i in range(num):
    digit = int(input())
    if digit >= 0:
        positive.append(digit)
    else:
        negative.append(digit)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
