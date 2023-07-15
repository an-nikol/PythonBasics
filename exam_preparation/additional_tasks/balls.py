from math import floor

number_of_balls = int(input())

total_points = 0

red_balls_counter = 0
orange_balls_counter = 0
yellow_balls_counter = 0
white_balls_counter = 0
divides_from_black = 0
other_colours_counter = 0

for ball in range(number_of_balls):
    colour_of_ball = input()

    if colour_of_ball == 'red':
        total_points += 5
        red_balls_counter += 1
    elif colour_of_ball == 'orange':
        total_points += 10
        orange_balls_counter += 1
    elif colour_of_ball == 'yellow':
        total_points += 15
        yellow_balls_counter += 1
    elif colour_of_ball == 'white':
        total_points += 20
        white_balls_counter += 1
    elif colour_of_ball == 'black':
        total_points /= 2
        floor(total_points)
        divides_from_black += 1
    else:
        total_points = total_points
        other_colours_counter += 1

print(f'Total points: {int(total_points)}')
print(f'Red balls: {red_balls_counter}')
print(f'Orange balls: {orange_balls_counter}')
print(f'Yellow balls: {yellow_balls_counter}')
print(f'White balls: {white_balls_counter}')
print(f'Other colors picked: {other_colours_counter}')
print(f'Divides from black balls: {divides_from_black}')
