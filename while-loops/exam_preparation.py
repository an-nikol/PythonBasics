max_bad_grades = int(input())
bad_grades_counter = 0
average_grade = 0
total_problems_solved = 0
last_problem_solved = ''
is_failed = False

current_problem = input()
while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == max_bad_grades:
            is_failed = True
            break


    average_grade += current_grade
    total_problems_solved += 1
    last_problem_solved = current_problem
    current_problem = input()

if is_failed:
    print(f'You need a break, {bad_grades_counter} poor grades.')
else:
    print(f'Average score: {average_grade / total_problems_solved:.2f}')
    print(f'Number of problems: {total_problems_solved}')
    print(f'Last problem: {last_problem_solved}')
