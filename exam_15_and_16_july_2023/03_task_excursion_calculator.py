number_of_people = int(input())
season = input()

price_per_person = 0

if season == 'spring':
    if number_of_people <= 5:
        price_per_person += 50
    elif number_of_people > 5:
        price_per_person += 48

elif season == 'summer':
    if number_of_people <= 5:
        price_per_person += 48.50
        price_per_person *= 0.85
    elif number_of_people > 5:
        price_per_person += 45
        price_per_person *= 0.85

elif season == 'autumn':
    if number_of_people <= 5:
        price_per_person += 60
    elif number_of_people > 5:
        price_per_person += 49.50

elif season == 'winter':
    if number_of_people <= 5:
        price_per_person += 86.00
        price_per_person *= 1.08
    elif number_of_people > 5:
        price_per_person += 85.00
        price_per_person *= 1.08

total_sum = number_of_people * price_per_person
print(f'{total_sum:.2f} leva.')
