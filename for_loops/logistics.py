number_of_loads = int(input())

load_mikrobus = 0
load_truck = 0
load_train = 0

for i in range(1, number_of_loads + 1):
    load = int(input())
    if load <= 3:
        load_mikrobus += load
    elif 4 <= load <= 11:
        load_truck += load
    elif load >= 12:
        load_train += load

total_loads = load_mikrobus + load_train + load_truck

price_load_mikrobus = load_mikrobus * 200
price_load_truck = load_truck * 175
price_load_train = load_train * 120

average = (price_load_mikrobus + price_load_truck + price_load_train) / total_loads

percentage_mikrobus = load_mikrobus / total_loads * 100
percentage_truck = load_truck / total_loads * 100
percentage_train = load_train / total_loads * 100

print(f'{average:.2f}')
print(f'{percentage_mikrobus:.2f}%')
print(f'{percentage_truck:.2f}%')
print(f'{percentage_train:.2f}%')


