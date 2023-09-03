type_of_fruit = input()
package_size = input()
number_of_ordered_packages = int(input())

price_per_set = 0

if type_of_fruit == 'Watermelon':
    if package_size == 'small':
        price_per_set = 2 * 56
    elif package_size == 'big':
        price_per_set = 5 * 28.70

elif type_of_fruit == 'Mango':
    if package_size == 'small':
        price_per_set = 2 * 36.66
    elif package_size == 'big':
        price_per_set = 5 * 19.60

elif type_of_fruit == 'Pineapple':
    if package_size == 'small':
        price_per_set = 2 * 42.10
    elif package_size == 'big':
        price_per_set = 5 * 24.80
elif type_of_fruit == 'Raspberry':
    if package_size == 'small':
        price_per_set = 2 * 20
    elif package_size == 'big':
        price_per_set = 5 * 15.20

total_price = number_of_ordered_packages * price_per_set

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f'{total_price:.2f} lv.')
