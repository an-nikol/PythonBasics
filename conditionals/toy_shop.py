price_trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

total_price_puzzle = puzzles * 2.60
total_price_doll = dolls * 3
total_price_bear = bears * 4.10
total_price_minion = minions * 8.20
total_price_truck = trucks * 2

total_sum = total_price_puzzle + total_price_doll + total_price_bear + total_price_minion + total_price_truck
total_number_toys = puzzles + dolls + bears + minions + trucks

if total_number_toys >= 50:
   total_sum = total_sum - (total_sum * 0.25)

rent = total_sum * 0.10
total_sum = total_sum - rent

money_left = abs(total_sum - price_trip)

if total_sum >= price_trip:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')

