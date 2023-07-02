age = int(input())
laundry = float(input())
price_per_toy = int(input())

total_money = 0
current_birthday_money = 0
total_toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1

total_money += total_toys * price_per_toy
difference = abs(total_money - laundry)

if total_money >= laundry:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
