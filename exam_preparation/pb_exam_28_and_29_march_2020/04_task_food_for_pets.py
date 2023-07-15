number_of_days = int(input())
total_volume_food = float(input())

biscuits_counter = 0
percent_eaten_food = 0
total_dog_eaten_food = 0
total_cat_eaten_food = 0
total_eaten_food = 0
for day in range(1, number_of_days + 1):
    eaten_cat_food = int(input())
    eaten_dog_food = int(input())
    total_cat_eaten_food += eaten_cat_food
    total_dog_eaten_food += eaten_dog_food
    if day % 3 == 0:
        biscuits_counter += (eaten_dog_food + eaten_cat_food) * 0.10

total_eaten_food = total_cat_eaten_food + total_dog_eaten_food
percent_eaten_food = total_eaten_food / total_volume_food * 100
percent_cat_eaten_food = total_cat_eaten_food / total_eaten_food * 100
percent_dog_eaten_food = total_dog_eaten_food / total_eaten_food * 100

print(f'Total eaten biscuits: {round(biscuits_counter)}gr.')
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f'{percent_cat_eaten_food:.2f}% eaten from the dog.')
print(f'{percent_dog_eaten_food:.2f}% eaten from the cat.')
