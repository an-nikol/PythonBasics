inheritance_money = float(input())
year = int(input())
age = 18
for years in range(1800, year + 1):
    if years % 2 == 0:
        inheritance_money -= 12000
    else:
        inheritance_money -= 12000 + (50 * age)
    age += 1

if inheritance_money >= 0:
    print(f'Yes! He will live a carefree life and will have {inheritance_money:.2f} dollars left.')
else:
    print(f"He will need {abs(inheritance_money):.2f} dollars to survive.")
