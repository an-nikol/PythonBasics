chicken_menu = int(input())
fish_menu = int(input())
vegetarians_menu = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegatarians_menu = 8.15
price_delivery = 2.50

total_chicken_menu = chicken_menu * price_chicken_menu
total_fish_menu = fish_menu * price_fish_menu
total_vegatarians_menu = vegetarians_menu * price_vegatarians_menu

total_sum_main_menu = total_chicken_menu + total_fish_menu + total_vegatarians_menu
price_desert = total_sum_main_menu * 0.20

result = total_sum_main_menu + price_desert + price_delivery
print('цена на поръчката', result)
