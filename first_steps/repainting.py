nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
all_hours_workers = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
bags = 0.40

final_price_nylon = (nylon_needed + 2) * price_nylon
final_price_paint = (paint_needed + 10/100 * paint_needed) * price_paint
final_price_thinner = thinner_needed * price_thinner
sum_materials = final_price_nylon + final_price_paint + final_price_thinner + bags
final_price_working_hours = (sum_materials * 30/100) * all_hours_workers
total = sum_materials + final_price_working_hours

print('сумата на всички разходи', total)
