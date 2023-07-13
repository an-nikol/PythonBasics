start_of_interval = input()
end_of_interval = input()
pass_letter = input()

start = ord(start_of_interval)
stop = ord(end_of_interval) + 1
pass_letter = ord(pass_letter)
my_range = range(start, stop)

counter = 0

for i in my_range:
    if i == pass_letter:
        continue
    for k in my_range:
        if k == pass_letter:
            continue
        for j in my_range:
            if j == pass_letter:
                continue
            ord_to_char_1 = chr(i)
            ord_to_char_2 = chr(k)
            ord_to_char_3 = chr(j)
            print(f'{ord_to_char_1}{ord_to_char_2}{ord_to_char_3}' + ' ', end='')
            counter += 1

print(counter)
