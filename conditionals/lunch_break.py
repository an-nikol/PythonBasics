from math import ceil
serial = input()
serial_time = int(input())
lunch_break = int(input())

lunch = lunch_break * 1/8
peace_time = lunch_break * 1/4

time_for_watching = lunch_break - (lunch + peace_time)


left_time = abs(time_for_watching - serial_time)
left_time = ceil(left_time)

if serial_time <= time_for_watching:
 print(f'You have enough time to watch {serial} and left with {left_time} minutes free time.')
else:
 print(f"You don't have enough time to watch {serial}, you need {left_time} more minutes.")
