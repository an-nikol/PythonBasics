number_of_students = int(input())

group_2_299 = 0
group_3_399 = 0
group_4_499 = 0
group_5_and_above = 0

all_marks = 0

for student in range(1, number_of_students + 1):
    current_mark = float(input())
    all_marks += current_mark

    if 2 <= current_mark <= 2.99:
        group_2_299 += 1
    elif 3 <= current_mark <= 3.99:
        group_3_399 += 1
    elif 4 <= current_mark <= 4.99:
        group_4_499 += 1
    else:
        group_5_and_above += 1

percentage_top_students = group_5_and_above / number_of_students * 100
percentage_between_4_and_499 = group_4_499 / number_of_students * 100
percentage_between_3_and_399 = group_3_399 / number_of_students * 100
percentage_between_2_and_299 = group_2_299 / number_of_students * 100

average = all_marks / number_of_students

print(f'Top students: {percentage_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percentage_between_4_and_499:.2f}%')
print(f'Between 3.00 and 3.99: {percentage_between_3_and_399:.2f}%')
print(f'Fail: {percentage_between_2_and_299:.2f}%')
print(f'Average: {average:.2f}')
