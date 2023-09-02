product = input()
city = input()
qty = float(input())

price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = qty * 0.5
    elif product == 'water':
        price = qty * 0.8
    elif product == 'beer':
        price = qty * 1.2
    elif product == 'sweets':
        price = qty * 1.45
    elif product == 'peanuts':
        price = qty * 1.60

if city == 'Plovdiv':
    if product == 'coffee':
        price = qty * 0.4
    elif product == 'water':
        price = qty * 0.7
    elif product == 'beer':
        price = qty * 1.15
    elif product == 'sweets':
        price = qty * 1.30
    elif product == 'peanuts':
        price = qty * 1.50

if city == 'Varna':
    if product == 'coffee':
        price = qty * 0.45
    elif product == 'water':
        price = qty * 0.7
    elif product == 'beer':
        price = qty * 1.1
    elif product == 'sweets':
        price = qty * 1.35
    elif product == 'peanuts':
        price = qty * 1.55

print(price)
