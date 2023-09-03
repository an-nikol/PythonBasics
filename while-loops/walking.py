target_steps = 10000
total_steps_a_day = 0

while total_steps_a_day < target_steps:
    command = input()
    if command == 'Going home':
        last_steps = int(input())
        total_steps_a_day += last_steps
        break

    current_steps = int(command)# transform it to int 
    total_steps_a_day += current_steps

diff = abs(target_steps - total_steps_a_day)

if total_steps_a_day >= target_steps:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
