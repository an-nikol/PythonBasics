projection = input()
rows = int(input())
colons = int(input())

price = 0

if projection == 'Premiere':
    price = (rows * colons) * 12.00
elif projection == 'Normal':
    price = (rows * colons) * 7.50
elif projection == 'Discount':
    price = (rows * colons) * 5.00

print(f'{price:.2f} leva')
