month = input()
number_of_nights = int(input())

studio_rent = 0
apartment_rent = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65

    if number_of_nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
    elif number_of_nights > 7:
        studio_price *= 0.95

    studio_rent = number_of_nights * studio_price
    apartment_rent = number_of_nights * apartment_price


elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70

    if number_of_nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90

    studio_rent = number_of_nights * studio_price
    apartment_rent = number_of_nights * apartment_price


elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

    if number_of_nights > 14:
        apartment_price *= 0.90

    studio_rent = number_of_nights * studio_price
    apartment_rent = number_of_nights * apartment_price

print(f'Apartment: {apartment_rent:.2f} lv.')
print(f'Studio: {studio_rent:.2f} lv.')

