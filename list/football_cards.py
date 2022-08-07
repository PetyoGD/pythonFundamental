game_str = input().split()
player_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
player_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
flag = False
for player in game_str:
    if player in player_a:
        player_a.remove(player)
    elif player in player_b:
        player_b.remove(player)
    if len(player_a) < 7 or len(player_b) < 7:
        flag = True
        break
print(f"Team A - {len(player_a)}; Team B - {len(player_b)}")
if flag:
    print("Game was terminated")
