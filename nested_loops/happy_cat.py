number_of_days = int(input())
hours_parking = int(input())

counter_days = 0
total = 0

are_parking_hours_reached = False

for day in range(1, number_of_days + 1):
    counter_days += 1
    price_per_day = 0
    for hour in range(1, 25):
        if hour > hours_parking:
            are_parking_hours_reached = True
            break

        if day % 2 == 0 and hour % 2 == 1:
            price_per_hour = 2.50
            price_per_day += price_per_hour
        elif day % 2 == 1 and hour % 2 == 0:
            price_per_hour = 1.25
            price_per_day += price_per_hour
        else:
            price_per_hour = 1
            price_per_day += price_per_hour

    total += price_per_day 
    print(f'Day: {counter_days} - {price_per_day:.2f} leva')

print(f'Total: {total:.2f} leva')
