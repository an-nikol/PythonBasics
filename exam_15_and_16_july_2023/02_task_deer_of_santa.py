from math import floor
from math import ceil


number_of_days_absent = int(input())
total_food_left = int(input())  
food_per_day_for_first_deer = float(input())
food_per_day_for_second_deer = float(input())
food_per_day_for_third_deer = float(input())

first_deer_total_food = food_per_day_for_first_deer * number_of_days_absent
second_deer_total_food = food_per_day_for_second_deer * number_of_days_absent
third_deer_total_food = food_per_day_for_third_deer * number_of_days_absent

total_needed_food = first_deer_total_food + second_deer_total_food +third_deer_total_food

diff = abs(total_needed_food - total_food_left)

if total_food_left > total_needed_food:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
