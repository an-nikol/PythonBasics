budget = int(input())
season = input()
number_of_fishers = int(input())

rent_a_boat = 0

if season == 'Spring':
    rent_a_boat = 3000
elif season == 'Summer' or season == 'Autumn':
    rent_a_boat = 4200
elif season == 'Winter':
    rent_a_boat = 2600

if number_of_fishers <= 6:
    rent_a_boat *= 0.90
elif 7 <= number_of_fishers <= 11:
    rent_a_boat *= 0.85
elif number_of_fishers >= 12:
    rent_a_boat *= 0.75

if number_of_fishers % 2 == 0 and season != 'Autumn':
    rent_a_boat *= 0.95

money_left = abs(budget - rent_a_boat)

if budget >= rent_a_boat:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')
