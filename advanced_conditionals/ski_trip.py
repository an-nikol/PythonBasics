number_of_days = int(input())
type_of_room = input()
mark = input()

price_for_night = 0

if type_of_room == 'room for one person':
    price_for_night = 18
    total = (number_of_days * price_for_night) - price_for_night

elif type_of_room == 'apartment':
    price_for_night = 25
    if number_of_days < 10:
        price_for_night *= 0.70
        total = (number_of_days * price_for_night) - price_for_night
    elif 10 <= number_of_days <= 15:
        price_for_night *= 0.65
        total = (number_of_days * price_for_night) - price_for_night
    elif number_of_days > 15:
        price_for_night *= 0.50
        total = (number_of_days * price_for_night) - price_for_night
    else:
        total = (number_of_days * price_for_night) - price_for_night

elif type_of_room == 'president apartment':
    price_for_night = 35
    if number_of_days < 10:
        price_for_night *= 0.90
        total = (number_of_days * price_for_night) - price_for_night
    elif 10 <= number_of_days <= 15:
        price_for_night *= 0.85
        total = (number_of_days * price_for_night) - price_for_night
    elif number_of_days > 15:
        price_for_night *= 0.80
        total = (number_of_days * price_for_night) - price_for_night
    else:
        total = (number_of_days * price_for_night) - price_for_night

if mark == 'positive':
    total *= 1.25
else:
    total *= 0.90

(print(f'{total:.2f}'))

