flower = input()
number_of_flowers = int(input())
budget = int(input())

price_per_flower = 0



if flower == 'Roses':
    price_per_flower = 5
    if number_of_flowers > 80:
        price_per_flower *= 0.9

elif flower == 'Dahlias':
    price_per_flower = 3.8
    if number_of_flowers > 90:
        price_per_flower *= 0.85

elif flower == 'Tulips':
    price_per_flower = 2.8
    if number_of_flowers > 80:
        price_per_flower *= 0.85

elif flower == 'Narcissus':
    price_per_flower = 3
    if number_of_flowers < 120:
        price_per_flower *= 1.15

elif flower == 'Gladiolus':
    price_per_flower = 2.5
    if number_of_flowers < 80:
        price_per_flower *= 1.20

total_sum = price_per_flower * number_of_flowers
money_left = abs(budget - total_sum)

if budget >= total_sum:
    print(f'Hey, you have a great garden with {number_of_flowers} {flower} and {money_left:.2f} leva left.')
else:
    print(f'Not enough money, you need {money_left:.2f} leva more.')
