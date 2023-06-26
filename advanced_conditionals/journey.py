budget = float(input())
season = input()

destination = ''
rent_type = ''
spent_money = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spent_money = budget * 0.3
    elif season == 'winter':
        spent_money = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spent_money = budget * 0.4
    elif season == 'winter':
        spent_money = budget * 0.8
else:
    destination = 'Europe'
    spent_money = budget * 0.9

if season == 'summer' and destination != 'Europe':
    rest_type = 'Camp'
else:
    rest_type = 'Hotel'

print(f'Somewhere in {destination}')
print (f'{rest_type} - {spent_money:.2f}')
