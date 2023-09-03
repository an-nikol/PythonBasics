start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())

combination_counter = 0
condition_for_validity = False
print_data = ''

for num_1 in range(start_of_interval, end_of_interval + 1):
    for num_2 in range(start_of_interval, end_of_interval + 1):
        combination_counter += 1 
        if num_1 + num_2 == magic_number:
            condition_for_validity = True
            print_data = f'Combination N:{combination_counter} ({num_1} + {num_2} = {magic_number})'
            break

    if condition_for_validity:
        break

if condition_for_validity:
    print(print_data)
else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')
