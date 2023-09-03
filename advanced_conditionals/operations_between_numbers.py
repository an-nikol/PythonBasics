number_one = int(input())
number_two = int(input())
operator = input()

result = 0


if operator == '+' or operator == '-' or operator == '*':
    type_of_number = ''
    if operator == '+':
        result = number_one + number_two
    elif operator == '-':
        result = number_one - number_two
    elif operator == '*':
        result = number_one * number_two

    if result % 2 == 0:
        type_of_number = 'even'
    else:
        type_of_number = 'odd'
    print(f'{number_one} {operator} {number_two} = {result} - {type_of_number}')


elif operator == '/':
    if number_two == 0:
        print(f'Cannot divide {number_one} by zero')
    else:
        result = number_one / number_two
        print(f'{number_one} / {number_two} = {result:.2f}')

elif operator == '%':
    if number_two == 0:
        print(f'Cannot divide {number_one} by zero')
    else:
        result = number_one % number_two
        print(f'{number_one} % {number_two} = {result}')

