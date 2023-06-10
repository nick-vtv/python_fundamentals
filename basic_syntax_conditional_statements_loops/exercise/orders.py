number_of_orders = int(input())
total = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    order_price = days * capsules_per_day * price_per_capsule
    print(f'The price for the coffee is: ${order_price:.2f}')
    total += order_price
print(f'Total: ${total:.2f}')
