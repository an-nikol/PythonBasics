n = int(input())

for number in range(1111, 10000):
    is_special = True
    num_to_string = str(number)
    for char in range(len(num_to_string)):
        current_num = int(num_to_string[char])
        if current_num == 0 or n % current_num != 0:
            is_special = False
            break
    if is_special:
        print(number, end=' ')
