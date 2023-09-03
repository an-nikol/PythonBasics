n = int(input())

stars = 1
range_of_rows = 0

is_n_even = n % 2 == 0
dash = (n - stars) // 2


if is_n_even:
    range_of_rows = n // 2
    stars = 2
else:
    range_of_rows = n // 2 + 1


for row in range(int(range_of_rows)):
    print('-' * dash + '*' * stars + '-' * dash)
    stars += 2
    dash = (n-stars) // 2

other_rows = n - range_of_rows

for row in range (other_rows):
    print('|' + '*' * (n-2) + '|')
