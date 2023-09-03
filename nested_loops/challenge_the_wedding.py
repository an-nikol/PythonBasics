number_of_male_clients = int(input())
number_of_women_clients = int(input())
max_tables = int(input())

counter_seats = 0
is_restaurant_full = False

for men in range(1, number_of_male_clients + 1):
    for women in range(1, number_of_women_clients + 1):
        print(f'({men} <-> {women})', end=' ')
        counter_seats += 1
        if counter_seats >= max_tables:
            is_restaurant_full = True
            break
    if is_restaurant_full:
        break
