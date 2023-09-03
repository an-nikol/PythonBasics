book_looking = input()
number_of_books = 0
book_is_found = False

current_book = input()
while current_book != 'No More Books':
    if current_book == book_looking:
        book_is_found = True
        break

    number_of_books += 1
    current_book = input() # if this is not the book we are looking for, we create a new entrance
if book_is_found:
    print(f'You checked {number_of_books} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {number_of_books} books.')
