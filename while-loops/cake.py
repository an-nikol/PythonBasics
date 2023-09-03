width = int(input())
lenght = int(input())
no_more_cake = False
total_volume_cake = width * lenght

command = input()
while command != 'STOP':
    current_pieces = int(command)
    total_volume_cake -= current_pieces
    if total_volume_cake < 0:
        no_more_cake = True
        break

    command = input()

if no_more_cake:
    print(f'No more cake left! You need {abs(total_volume_cake)} pieces more.')
else:
    print(f'{total_volume_cake} pieces are left.')
