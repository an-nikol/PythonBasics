coffee_type = input()
sugar = input()
number_of_drinks = int(input())

price_per_drink = 0

if coffee_type == 'Espresso':
    if sugar == 'Without':
        price_per_drink = 0.90
        price_per_drink *= 0.65
    elif sugar == 'Normal':
        price_per_drink = 1
    elif sugar == 'Extra':
        price_per_drink = 1.20
    if number_of_drinks >= 5:
        price_per_drink *= 0.75

elif coffee_type == 'Cappuccino':
    if sugar == 'Without':
        price_per_drink = 1
        price_per_drink *= 0.65
    elif sugar == 'Normal':
        price_per_drink = 1.20
    elif sugar == 'Extra':
        price_per_drink = 1.60

elif coffee_type == 'Tea':
    price_per_drink = 0.50
    if sugar == 'Without':
        price_per_drink *= 0.65
    elif sugar == 'Normal':
        price_per_drink = 0.60
    elif sugar == 'Extra':
        price_per_drink = 0.70

total_sum = number_of_drinks * price_per_drink
if total_sum > 15:
    total_sum *= 0.80

print(f'You bought {number_of_drinks} cups of {coffee_type} for {total_sum:.2f} lv.')

