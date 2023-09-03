n = int(input())

star = ''
second_stars = ''
for row in range((n + 1) // 2):
    if row == 0:
        if n % 2 == 1:
            star = '*'
        else:
            star = '**'
    else:
        second_stars = star + 2 * star

        print('_' * (n // 2) + '*' + '_' * (n // 2))
        print('_' * ((n // 2) - 1) + '*' * (n - 2) + '_' * ((n // 2) - 1) )
        print('*' * n)

