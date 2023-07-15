budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_of_excessive_expenses = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95

total_price = number_of_nights * price_per_night
percent_of_excessive_expenses = budget * (percent_of_excessive_expenses / 100)
final_price = total_price + percent_of_excessive_expenses
diff = abs(budget - final_price)

if budget >= final_price:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
