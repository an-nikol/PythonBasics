budget = float(input())
videocards = int(input())
procesors = int(input())
ram = int(input())

price_videocards = videocards * 250
price_procesor = price_videocards * 0.35
price_ram = price_videocards * 0.10

total_sum_procesors = price_procesor * procesors
total_sum_ram = price_ram * ram


total_sum = price_videocards + total_sum_procesors + total_sum_ram

if videocards > procesors:
    total_sum *= 0.85

money_left = abs(total_sum - budget)

if total_sum <= budget:
    print(f'You have {money_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {money_left:.2f} leva more!')
