num1_max_limit = int(input())
num2_max_limit = int(input())
num3_max_limit = int(input())

for num1 in range(1, num1_max_limit + 1):
    if num1 % 2 == 1:
        continue
    for num2 in range(2, num2_max_limit + 1):
        for num3 in range(1, num3_max_limit + 1):
            if num3 % 2 == 1:
                continue
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f'{num1} {num2} {num3}')
