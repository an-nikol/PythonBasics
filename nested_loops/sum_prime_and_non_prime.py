is_prime = True
sum_prime = 0
sum_non_prime = 0


input_line = input()
while input_line != 'stop':
    number = int(input_line)
    if number < 0:
        print('Number is negative.')
    else:
        for i in range(2, number): 
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime += number
        else:
            sum_non_prime += number
            is_prime = True
    input_line = input()


print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
