room_num = int(input())
room_count = 0
free_chair = 0
flag = False
for room in range(room_num):
    info_series = input().split()
    room_count += 1
    chair_num = len(info_series[0])
    visitors_num = int(info_series[1])
    if chair_num >= visitors_num:
        free_chair += chair_num - visitors_num
        continue
    else:
        needed = visitors_num - chair_num
        flag = True
        print(f"{needed} more chairs needed in room {room_count}")
if not flag:
    print(f"Game On, {free_chair} free chairs left")
