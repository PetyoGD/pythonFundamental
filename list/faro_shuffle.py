card_deck = input().split()
num_shuffle = int(input())
card_shuffle_list = []
temp_shuffle = 0
for numbers in range(num_shuffle):
    temp_shuffle = []
    middle_of_the_deck = len(card_deck) //2
    left_part = card_deck[0:middle_of_the_deck]
    right_part = card_deck[middle_of_the_deck::]
    for index in range(len(left_part)):
        temp_shuffle.append(left_part[index])
        temp_shuffle.append(right_part[index])
    card_deck = temp_shuffle
print(card_deck)
