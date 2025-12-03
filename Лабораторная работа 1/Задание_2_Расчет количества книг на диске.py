# TODO Найдите количество книг, которое можно разместить на дискете
diskette_size_mb = 1.44

pages_per_book = 100      # страниц в книге
lines_per_page = 50       # строк на странице
chars_per_line = 25       # символов в строке
bytes_per_char = 4        # байт на символ

bytes_per_kb = 1024       # 1 КБ = 1024 байта
kb_per_mb = 1024          # 1 МБ = 1024 КБ

book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char   # #Вычисляем размер одной книги в байтах (страницы × строки × символы × байт_на_символ)

diskette_size_bytes = diskette_size_mb * kb_per_mb * bytes_per_kb   #  Переводим объём дискеты в байты

books_count = int(diskette_size_bytes // book_size_bytes)   #Считаем, сколько книг поместится

print("Количество книг, помещающихся на дискету:", books_count)