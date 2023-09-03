n = int(input())

sum_numbers = 0
first_number = int(input())
sum_numbers += first_number
max_num = first_number

for i in range(n - 1):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

if max_num == sum_numbers - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (sum_numbers - max_num))
    print('No')
    print(f'Diff = {diff}')
