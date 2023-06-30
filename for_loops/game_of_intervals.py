number_of_intervals = int(input())

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_number = 0

points = 0

for i in range(number_of_intervals):
    current_position = int(input())

    if 0 <= current_position <= 9:
        points += current_position * 0.20
        from_0_to_9 += 1
    elif 10 <= current_position <= 19:
        points += current_position * 0.30
        from_10_to_19 += 1
    elif 20 <= current_position <= 29:
        points += current_position * 0.40
        from_20_to_29 += 1
    elif 30 <= current_position <= 39:
        points += 50
        from_30_to_39 += 1
    elif 40 <= current_position <= 50:
        points += 100
        from_40_to_50 += 1
    else:
        points /= 2
        invalid_number += 1

percentage_from_0_to_9 = from_0_to_9 / number_of_intervals * 100
percentage_from_10_to_19 = from_10_to_19 / number_of_intervals * 100
percentage_from_20_to_29 = from_20_to_29 / number_of_intervals * 100
percentage_from_30_to_39 = from_30_to_39 / number_of_intervals * 100
percentage_from_40_to_50 = from_40_to_50 / number_of_intervals * 100
percentage_invalid_numbers = invalid_number / number_of_intervals * 100


print(f'{points:.2f}')
print(f'From 0 to 9: {percentage_from_0_to_9:.2f}%')
print(f'From 10 to 19: {percentage_from_10_to_19:.2f}%')
print(f'From 20 to 29: {percentage_from_20_to_29:.2f}%')
print(f'From 30 to 39: {percentage_from_30_to_39:.2f}%')
print(f'From 40 to 50: {percentage_from_40_to_50:.2f}%')
print(f'Invalid numbers: {percentage_invalid_numbers:.2f}%')
