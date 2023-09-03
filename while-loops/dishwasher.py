bottles_of_liquids = int(input())

no_liquid = False
counter = 1
total_liquid = bottles_of_liquids * 750
number_of_dishes = 0
number_of_pots = 0

command = input()
while command != 'End':
    dishes = int(command)
    if counter % 3 == 0:
        total_liquid -= dishes * 15
        number_of_pots += dishes
        counter += 1
    else:
        total_liquid -= dishes * 5
        number_of_dishes += dishes
        counter += 1

    if total_liquid < 0:
        no_liquid = True
        break

    command = input()

if no_liquid:
    print(f'Not enough detergent, {abs(total_liquid)} ml. more necessary!')
else:
    print(f'Detergent was enough!')
    print(f'{number_of_dishes} dishes and {number_of_pots} pots were washed.')
    print(f'Leftover detergent {total_liquid} ml.')
