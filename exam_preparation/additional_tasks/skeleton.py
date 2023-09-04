minutes_of_control = int(input())
seconds_of_control = int(input())
length = float(input())
seconds_for_100_m = int(input())

total_control_time_to_seconds = (minutes_of_control * 60) + seconds_of_control
times_he_will_be_slowed = length / 120
total_decreased_time = times_he_will_be_slowed * 2.5
time_of_marin = (length / 100) * seconds_for_100_m - total_decreased_time

if time_of_marin <= total_control_time_to_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_of_marin:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(total_control_time_to_seconds - time_of_marin):.3f} second slower.')
