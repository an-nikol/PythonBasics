width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
no_more_space = False

command = input()
while command != 'Done':
    command = int(command)
    total_volume -= command
    if total_volume < 0:
        no_more_space = True
        break
    command = input()

if no_more_space:
    print(f'No more free space! You need {abs(total_volume)} Cubic meters more.')
else:
    print(f'{abs(total_volume)} Cubic meters left.')
