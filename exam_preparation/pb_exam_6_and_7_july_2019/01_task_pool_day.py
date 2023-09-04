from math import ceil

number_of_people = int(input())
tax_for_entrance = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

total_tax = number_of_people * tax_for_entrance
number_of_chairs = ceil(number_of_people * 0.75)
total_price_chairs = number_of_chairs * price_per_chair
number_of_umbrellas = ceil(number_of_people * 0.50)
total_price_umbrella = number_of_umbrellas * price_per_umbrella

final_price = total_tax + total_price_chairs + total_price_umbrella

print(f'{final_price:.2f} lv.')
