name_actor = input()
points_academia = float(input())
number_of_examiners = int(input())

total_points = points_academia

for i in range(number_of_examiners):
    name_of_examiner = input()
    points_from_examiner = float(input())
    current_points = len(name_of_examiner) * points_from_examiner / 2
    total_points += current_points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = abs(1250.5 - total_points)
    print(f'Sorry, {name_actor} you need {diff:.1f} more!')
