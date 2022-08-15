def odd_even_sum(number):
    even = 0
    odd = 0
    for num in range(len(digit)):
        num = int(digit[num])
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return even, odd


digit = int(input())
digit = str(digit)
even, odd = odd_even_sum(digit)
print(f"Odd sum = {odd}, Even sum = {even}")
