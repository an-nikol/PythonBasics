budget_film = float(input())
number_statists = int(input())
price_clothing_statist = float(input())

decor = budget_film * 0.10

if number_statists > 150:
    price_clothing_statist = price_clothing_statist - (price_clothing_statist * 0.10)

total_price_clothing = price_clothing_statist * number_statists

total_expenses = total_price_clothing + decor
money_left = abs(budget_film - total_expenses)

if total_expenses > budget_film:
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
