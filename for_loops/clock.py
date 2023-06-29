total_time = 1440

hours = 0
minutes = 0

for i in range(24):

    if i == 0:
        hours = 0
        minutes = 0
        print(f'{hours}:{minutes:02d}')

    if i != 0:
        minutes += 1
        if minutes > 60:
            hours += 1
        print(f'{hours}:{minutes:02d}')
