money_for_trip = float(input())
money_owned = float(input())
days_counter = 0
spending_counter = 0

while money_owned < money_for_trip and spending_counter < 5:
    command = input()
    current_money = float(input())
    days_counter += 1
    if command == 'save':
        money_owned += current_money
        spending_counter = 0
    elif command == 'spend':
        money_owned -= current_money
        spending_counter += 1
        if money_owned < 0:
            money_owned = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)

if money_owned >= money_for_trip:
    print(f'You saved the money for {days_counter} days.')

