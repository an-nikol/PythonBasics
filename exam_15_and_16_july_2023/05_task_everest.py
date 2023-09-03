starting_point = 5364
goal = 8848
days_counter = 1

current_climbed_distance = starting_point

while True:
    is_he_resting = input()
    if is_he_resting == 'END':
        break

    climbed_meters = int(input())

    if is_he_resting == 'Yes':
        days_counter += 1
        if days_counter > 5:
            break

    current_climbed_distance += climbed_meters
    if current_climbed_distance >= goal:
        break

if current_climbed_distance >= goal:
    print(f'Goal reached for {days_counter} days!')
else:
    print('Failed!')
    print(f'{current_climbed_distance}')
