control_number_m = int(input())

counter = 0
fourth_num = 0

pass_first_char = 0
pass_second_char = 0
pass_third_char = 0
pass_fourth_char = 0

is_combination_valid = False
for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if num1 < num2 and num3 > num4:
                    if (num1 * num2) + (num3 * num4) == control_number_m:
                        print(f'{num1}{num2}{num3}{num4}' + ' ', end='')
                        counter += 1
                        if counter == 4:
                            pass_first_char = num1
                            pass_second_char = num2
                            pass_third_char = num3
                            pass_fourth_char = num4
                            is_combination_valid = True

print()
if is_combination_valid:
    print(f'Password: {pass_first_char}{pass_second_char}{pass_third_char}{pass_fourth_char}')
else:
    print('No!')
