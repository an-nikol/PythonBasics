bought_food_kg = int(input())
bought_food_kg_to_gr = bought_food_kg * 1000

total_eaten_food = 0
command = input()
while command != 'Adopted':
    grams_eaten_per_meal = int(command)
    total_eaten_food += grams_eaten_per_meal
    command = input()

if bought_food_kg_to_gr >= total_eaten_food:
    print(f'Food is enough! Leftovers: {bought_food_kg_to_gr - total_eaten_food} grams.')
else:
    print(f'Food is not enough. You need {abs(bought_food_kg_to_gr - total_eaten_food)} grams more.')
