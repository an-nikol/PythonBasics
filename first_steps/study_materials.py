pack_pens = int(input())
pack_markers = int(input())
liters_spray = int(input())
discount_percent = int(input())

price_pack_pens = 5.80
price_pack_markers = 7.20
price_liters_spray = 1.20

pens_sum = pack_pens * price_pack_pens
markers_sum = pack_markers * price_pack_markers
liters_sum = liters_spray * price_liters_spray

sum = pens_sum + markers_sum + liters_sum
total_sum = sum - (sum * discount_percent) / 100

print(total_sum)
