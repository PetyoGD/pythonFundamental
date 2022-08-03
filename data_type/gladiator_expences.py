lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_price_corr = lost_fight // 2
sword_price_corr = lost_fight // 3
shield_price_corr = lost_fight // 6
armor_price_corr = lost_fight // 12
total_price = helmet_price_corr * helmet_price + sword_price_corr * sword_price \
              + shield_price_corr * shield_price + armor_price_corr * armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
