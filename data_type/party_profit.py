number_companion = int(input())
day = int(input())
companion = number_companion
gathered_coins = 0
for i in range(1, day + 1):
    if i % 10 == 0:
        companion -= 2
    if i % 15 == 0:
        companion += 5
    if i % 3 == 0:
        gathered_coins -= companion * 3
    if i % 5 == 0:
        gathered_coins += companion * 20
        if i % 3 == 0:
            gathered_coins -= companion * 2
    gathered_coins += 50
    gathered_coins -= companion * 2
coins = int(gathered_coins / companion)
print(f"{companion} companions received {coins} coins each.")
