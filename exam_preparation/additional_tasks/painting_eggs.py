size_of_eggs = input()
colour_of_eggs = input()
number_of_packages = int(input())

profit = 0

if size_of_eggs == 'Large':
    if colour_of_eggs == 'Red':
        profit += 16
    elif colour_of_eggs == 'Green':
        profit += 12
    elif colour_of_eggs == 'Yellow':
        profit += 9

elif size_of_eggs == 'Medium':
    if colour_of_eggs == 'Red':
        profit += 13
    elif colour_of_eggs == 'Green':
        profit += 9
    elif colour_of_eggs == 'Yellow':
        profit += 7

elif size_of_eggs == 'Small':
    if colour_of_eggs == 'Red':
        profit += 9
    elif colour_of_eggs == 'Green':
        profit += 8
    elif colour_of_eggs == 'Yellow':
        profit += 5

expenses = (profit * number_of_packages) * 0.35
total_sum = (profit * number_of_packages) - expenses

print(f'{total_sum:.2f} leva.')
