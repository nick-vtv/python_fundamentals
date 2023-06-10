budget = float(input())
price_of_flour = float(input())
price_of_eggs = price_of_flour * 0.75
price_of_milk = price_of_flour * 1.25
bread_price = price_of_eggs + price_of_flour + (price_of_milk * 0.25)
breads = 0
colored_eggs = 0
while budget > 0:
    if budget - bread_price < 0:
        break
    budget -= bread_price
    breads += 1
    colored_eggs += 3
    if breads % 3 == 0:
        colored_eggs -= breads - 2
print(f'You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
