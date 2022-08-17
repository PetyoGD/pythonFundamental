number_series = [int(s) for s in input().split(", ")]
positive = []
negative = []
even = []
odd = []
for i in number_series:
    if i % 2 == 0:
        even.append(i)
    if i % 2 != 0:
        odd.append(i)
    if i >= 0:
        positive.append(i)
    if i < 0:
        negative.append(i)
print(f"Positive: {', '.join(str(s) for s in positive)}")
print(f"Negative: {', '.join(str(s) for s in negative)}")
print(f"Even: {', '.join(str(s) for s in even)}")
print(f"Odd: {', '.join(str(s) for s in odd)}")

# def positive_numbers(number_series):
#     return [str(s) for s in number_series if s >= 0]
#
#
# def negative_numbers(number_series):
#     return [str(n) for n in number_series if n < 0]
#
#
# def even_numbers(number_series):
#     return [str(e) for e in number_series if e % 2 == 0]
#
#
# def odd_numbers(number_series):
#     return [str(o) for o in number_series if o % 2 != 0]
#
#
# number_series = [int(s) for s in input().split(", ")]
#
# print(f"Positive: {', '.join(positive_numbers(number_series))}")