name = input()

average_grade = 0
next_class = 1
fails = 0

while True:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails > 1:
            print(f'{name} has been excluded at {next_class} grade')
            break
        continue
    next_class += 1
    average_grade += current_grade
    if next_class > 12:
        print(f'{name} graduated. Average grade: {average_grade / 12:.2f}')
        break
