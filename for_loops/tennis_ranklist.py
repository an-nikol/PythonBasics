number_of_competitions = int(input())
starting_points = int(input())
total_points = 0
competitions_won = 0

for i in range(number_of_competitions):
    stage_of_competition = input()
    if stage_of_competition == 'W':
        total_points += 2000
        competitions_won += 1
    elif stage_of_competition == 'F':
        total_points += 1200
    elif stage_of_competition == 'SF':
        total_points += 720

total_points += starting_points
average_points = (total_points - starting_points) // number_of_competitions
percentage_of_won_competitions = competitions_won / number_of_competitions * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percentage_of_won_competitions:.2f}%')
