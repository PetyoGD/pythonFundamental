allowed_quantity = int(input())
days_to_christmas = int(input())
christmas_spirit = 0
ornament_set_price = 0
tree_skirt_price = 0
tree_garlands_prise = 0
tree_lights_price = 0
for day in range(1, days_to_christmas + 1):
    if day % 2 == 0:
        ornament_set_price += allowed_quantity * 2
        christmas_spirit += 5
    if day % 3 == 0:
        tree_skirt_price += allowed_quantity * 5
        tree_garlands_prise += allowed_quantity * 3
        christmas_spirit += 13
    if day % 5 == 0:
        tree_lights_price += allowed_quantity * 15
        christmas_spirit += 17
        if allowed_quantity == 3:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        tree_skirt_price += 5
        tree_garlands_prise += 3
        tree_lights_price += 15
        if days_to_christmas % 10 == 0:
            christmas_spirit -= 30
    if day % 11 == 0:
        allowed_quantity += 2
all_sum = ornament_set_price + tree_skirt_price + tree_garlands_prise + tree_lights_price
print(f"Total cost: {all_sum}")
print(f"Total spirit: {christmas_spirit}")
