period = int(input())

electricity = 0
water = 20
internet = 15
other = 0
total_electricity = 0

for month in range(period):
    electricity = float(input())
    sum = (electricity + water + internet) * 0.20
    other += electricity + water + internet + sum
    total_electricity += electricity


total_water = water * period
total_internet = internet * period

average = (total_electricity + total_water + total_internet + other) / period

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
