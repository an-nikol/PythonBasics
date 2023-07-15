starting_first_index_first_num = int(input())
starting_second_index_first_num = int(input())

starting_first_index_second_num = int(input())
starting_second_index_second_num = int(input())

counter = 0
is_not_valid = False

for num1 in range(starting_first_index_first_num, 9):
    if num1 % 2 == 1:
        continue
    for num2 in range(9, starting_second_index_first_num - 1, - 1):
        if num2 % 2 == 0:
            continue
        for num3 in range(starting_first_index_second_num, 9):
            if num3 % 2 == 1:
                continue
            for num4 in range(9, starting_second_index_second_num - 1, - 1):
                if num4 % 2 == 0:
                    continue
                if num1 == num3 and num2 == num4:
                    print('Cannot change the same player.')
                else:
                    print(f'{num1}{num2} - {num3}{num4}')
                    counter += 1
                    if counter > 6:
                        is_not_valid = True
                        break
            if is_not_valid:
                break
        if is_not_valid:
            break
    if is_not_valid:
        break
