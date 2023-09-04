from math import floor

name_of_serial = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
time_of_episode = float(input())

ads = time_of_episode * 0.20
final_time_per_episode = time_of_episode + ads
additional_special_time = number_of_seasons * 10

total_time = (final_time_per_episode * number_of_episodes * number_of_seasons) + additional_special_time

print(f'Total time needed to watch the {name_of_serial} series is {floor(total_time)} minutes.')


