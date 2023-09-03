number_of_judges = int(input())
total_grades_sum = 0
grades_counter = 0

command = input()
while command != 'Finish':
    grade = 0
    average_grade = 0

    for i in range(number_of_judges):
        grade += float(input())
        grades_counter += 1

    average_grade = grade / number_of_judges
    total_grades_sum += grade
    print(f'{command} - {average_grade:.2f}.')

    command = input()
    
average_grade_final = total_grades_sum / grades_counter
print(f"Student's final assessment is {average_grade_final:.2f}.")
