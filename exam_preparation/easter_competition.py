number_of_cakes = int(input())

best_points = 0
best_chef_name = ''

for i in range(number_of_cakes):
    sum_current_score = 0
    name_of_chef = input()

    command = input()
    while command != 'Stop':
        current_score = int(command)
        sum_current_score += current_score
        command = input()

    print(f'{name_of_chef} has {sum_current_score} points.')

    if sum_current_score > best_points:
        best_points = sum_current_score
        best_chef_name = name_of_chef
        print(f'{name_of_chef} is the new number 1!')

print(f'{best_chef_name} won competition with {best_points} points!')
