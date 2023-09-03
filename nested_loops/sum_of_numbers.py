start_of_interval = int(input())
end_of_interval = int(input())
magical_number = int(input())

counter = 0
is_found = False
for num1 in range(start_of_interval, end_of_interval + 1):
    for num2 in range(start_of_interval, end_of_interval + 1):
        counter += 1
        if num1 + num2 == magical_number:
            print(f'Combination N:{counter} ({num1} + {num2} = {magical_number})')
            is_found = True
            break
    if is_found:
        break


if not is_found:
    print(f'{counter} combinations - neither equals {magical_number}')
