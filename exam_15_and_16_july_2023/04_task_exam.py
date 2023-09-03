number_of_students = int(input())

mark_between_2_and_299 = 0
mark_between_3_and_399 = 0
mark_between_4_and_499 = 0
mark_between_5_and_above = 0

total_grades = 0

for student in range(1, number_of_students + 1):
    mark = float(input())

    if 2 <= mark <= 2.99:
        mark_between_2_and_299 += 1
        total_grades += mark
    elif 3 <= mark <= 3.99:
        mark_between_3_and_399 += 1
        total_grades += mark
    elif 4 <= mark <= 4.99:
        mark_between_4_and_499 += 1
        total_grades += mark
    else:
        mark_between_5_and_above += 1
        total_grades += mark

average = total_grades / number_of_students
percent_mark_between_5_and_above = (mark_between_5_and_above / number_of_students) * 100
percent_mark_between_4_and_499 = (mark_between_4_and_499 / number_of_students) * 100
percent_mark_between_3_and_399 = (mark_between_3_and_399 / number_of_students) * 100
percent_mark_between_2_and_299 = (mark_between_2_and_299 / number_of_students) * 100

print(f'Top students: {percent_mark_between_5_and_above:.2f}%')
print(f'Between 4.00 and 4.99: {percent_mark_between_4_and_499:.2f}%')
print(f'Between 3.00 and 3.99: {percent_mark_between_3_and_399:.2f}%')
print(f'Fail: {percent_mark_between_2_and_299:.2f}%')
