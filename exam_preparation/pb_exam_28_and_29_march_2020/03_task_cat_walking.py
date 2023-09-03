minutes_walking_per_day = int(input())
number_of_walks_per_day = int(input())
eaten_calories_per_day = int(input())

total_exercise = number_of_walks_per_day * minutes_walking_per_day

exercised_calories = total_exercise * 5

if exercised_calories >= eaten_calories_per_day / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {exercised_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {exercised_calories}.')
