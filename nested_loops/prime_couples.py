number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())

for num1 in range(number_one, (number_one + number_three + 1)):
    if num1 > 1:
        for i in range(2, num1 // 2):
            if (num1 % i) == 0:
                break
        else:
            for num2 in range(number_two, (number_two + number_four + 1)):
                if num2 > 1:
                    for i in range(2, num2 // 2):
                        if (num2 % i) == 0:
                            break
                    else:
                        print(f"{num1}{num2}")
