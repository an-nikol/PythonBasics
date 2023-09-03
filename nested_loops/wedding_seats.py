last_sector = input()
number_of_rows_first_sector = int(input())
number_of_seats_uneven_row = int(input())

number_of_seats_even_row = number_of_seats_uneven_row + 2
first_sector = 'A'
first_sector_to_ord = ord(first_sector)
last_sector_to_ord = ord(last_sector)

counter = 0

is_sector_full = False

for sector in range(first_sector_to_ord, last_sector_to_ord + 1):
    for row in range(1, number_of_rows_first_sector + 1):
        if row % 2 == 0:
            number_of_seats = number_of_seats_uneven_row + 2
        else:
            number_of_seats = number_of_seats_uneven_row

        last_character = 97 + number_of_seats
        for seat in range(97, last_character):
            sector_to_chr = chr(sector)
            seat_to_chr = chr(seat)
            print(f'{sector_to_chr}{row}{seat_to_chr}')
            counter += 1

    is_sector_full = True
    if is_sector_full:
        number_of_rows_first_sector += 1

print(counter)
