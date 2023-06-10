items_list = input().split("|")
budget = float(input())
valid_item = False
bought_items_prices_list = []
profit = 0
new_prices_total = 0
for item in items_list:
    current_item_list = item.split("->")
    if current_item_list[0] == 'Clothes' and float(current_item_list[1]) <= 50:
        valid_item = True
    elif current_item_list[0] == 'Shoes' and float(current_item_list[1]) <= 35:
        valid_item = True
    elif current_item_list[0] == 'Accessories' and float(current_item_list[1]) <= 20.50:
        valid_item = True
    if valid_item and float(current_item_list[1]) <= budget:
        budget -= float(current_item_list[1])
        new_price = float(current_item_list[1]) * 1.40
        new_prices_total += new_price
        bought_items_prices_list.append(str(f'{new_price:.2f}'))
        diff = new_price - (float(current_item_list[1]))
        profit += diff
    valid_item = False
print(" ".join(bought_items_prices_list))
print(f'Profit: {profit:.2f}')
if budget + new_prices_total >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
