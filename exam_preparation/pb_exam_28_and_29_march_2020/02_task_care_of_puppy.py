bought_dog_food = int(input())

kg_to_gr = bought_dog_food * 1000
command = input()
total_eaten_food = 0
while command != 'Adopted':
    food_per_meal = int(command)
    total_eaten_food += food_per_meal
    command = input()

if total_eaten_food <= kg_to_gr:
    print(f'Food is enough! Leftovers: {kg_to_gr - total_eaten_food} grams.')

else:
    print(f'Food is not enough. You need {abs(kg_to_gr - total_eaten_food)} grams more.')


