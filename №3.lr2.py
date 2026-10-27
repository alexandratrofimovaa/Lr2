import csv
from datetime import datetime

with open('books.csv', 'r') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))

with open('bibliography.txt', 'w', encoding='utf-8') as bibfile: #создание файла на русском языке
    count = 0
    used = []
    for row in table[1:]:
        author = row[3].strip()
        title = row[1].strip()
        key = (author, title)
        if key in used: #проверка на уникальность книги, которая попадёт в список
            continue
        year = datetime.strptime(row[6].split()[0], '%d.%m.%Y').year
        bibfile.write(f'{count + 1}. {author}. {title} - {year}\n')
        used.append(key)
        count += 1
        if count == 20:
            break
         

 