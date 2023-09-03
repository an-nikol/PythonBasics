min_number = int(input())

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    current_number = int(user_input)
    if current_number < min_number:
        min_number = current_number

print(min_number)
