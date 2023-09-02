fruit = input()
day = input()
qty = float(input())

price = 0
if_input_correct = True

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = qty * 2.50
    elif fruit == 'apple':
        price = qty * 1.20
    elif fruit =='orange':
        price = qty * 0.85
    elif fruit == 'grapefruit':
        price = qty * 1.45
    elif fruit == 'kiwi':
        price = qty * 2.70
    elif fruit == 'pineapple':
        price = qty * 5.50
    elif fruit == 'grapes':
        price = qty * 3.85
    else:
        if_input_correct = False


elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = qty * 2.70
    elif fruit == 'apple':
        price = qty * 1.25
    elif fruit =='orange':
        price = qty * 0.90
    elif fruit == 'grapefruit':
        price = qty * 1.60
    elif fruit == 'kiwi':
        price = qty * 3.00
    elif fruit == 'pineapple':
        price = qty * 5.60
    elif fruit == 'grapes':
        price = qty * 4.20
    else:
        if_input_correct = False
else:
       if_input_correct = False

#Print output

if if_input_correct:
    print(f'{price:.2f}')
else:
    print('error')
