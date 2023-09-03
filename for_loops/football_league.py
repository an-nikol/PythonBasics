seats_stadium = int(input())
all_fens = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(all_fens):
    current_fen = input()
    if current_fen == 'A':
        sector_a += 1
    elif current_fen == 'B':
        sector_b += 1
    elif current_fen == 'V':
        sector_v += 1
    elif current_fen == 'G':
        sector_g += 1

percentage_sector_a = sector_a / all_fens * 100
percentage_sector_b = sector_b / all_fens * 100
percentage_sector_v = sector_v / all_fens * 100
percentage_sector_g = sector_g / all_fens * 100

percentage_of_all_fens = all_fens / seats_stadium * 100

print(f'{percentage_sector_a:.2f}%')
print(f'{percentage_sector_b:.2f}%')
print(f'{percentage_sector_v:.2f}%')
print(f'{percentage_sector_g:.2f}%')
print(f'{percentage_of_all_fens:.2f}%')
