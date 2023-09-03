rent = float(input())

cake = rent * 0.20
drinks = cake - (cake * 0.45)
animator = rent * 1/3

budget = rent + cake + drinks + animator
print(budget)
