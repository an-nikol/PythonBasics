x = float(input())
y = float(input())
h = float(input())

front_and_back_walls = (x * x) * 2 - (1.2 * 2)
side_walls = (x * y) * 2 - 2 * (1.5 * 1.5)

roof = 2 * (x * y) + 2 * (x * h // 2)
