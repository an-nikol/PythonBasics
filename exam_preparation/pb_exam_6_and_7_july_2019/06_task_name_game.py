max_points = 0
winner = ''
name = input()
while name != "Stop":
    points = 0
    for letter in name:
        number = int(input())
        if number == ord(letter):
            points += 10
        else:
            points += 2
    if points >= max_points:
        winner = name
        max_points = points
    name = input()
print(f'The winner is {winner} with {max_points} points!')

