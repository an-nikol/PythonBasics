number_of_coins_1_lev = int(input())
number_of_coins_2_lev = int(input())
number_of_5_lev = int(input())
total_sum = int(input())


for i in range(number_of_coins_1_lev + 1):
    payment_1_lev = i * 1
    for j in range(number_of_coins_2_lev + 1):
        payment_2_lev = j * 2
        for k in range(number_of_5_lev + 1):
            payment_5_lev = k * 5
            if payment_1_lev + payment_2_lev + payment_5_lev == total_sum:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {total_sum} lv.')
