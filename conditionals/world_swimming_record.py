from math import floor

world_record = float(input())
meters = float(input())
time_one_meter = float(input())

time_ivan = meters * time_one_meter
time_ivan_with_delay = floor(meters / 15)
time_ivan_15 = time_ivan_with_delay * 12.5


full_time = time_ivan + time_ivan_15
seconds_left = abs(world_record - full_time)

if full_time < world_record:
    print(f'Yes, he succeeded! The new world record is {full_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {seconds_left:.2f} seconds slower.')
