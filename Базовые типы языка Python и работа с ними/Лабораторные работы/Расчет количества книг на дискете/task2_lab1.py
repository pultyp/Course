# TODO Найдите количество книг, которое можно разместить на дискете


size_in_mb = 1.44
pages_in_boook = 100
rows_on_page = 50
chars_in_row = 25
size_of_char_in_bytes = 4

size_of_one_book_in_mb = (size_of_char_in_bytes * chars_in_row * rows_on_page * pages_in_boook)/(1024*1024)

total_books = int(size_in_mb // size_of_one_book_in_mb)

print("Количество книг, помещающихся на дискету:", total_books)
