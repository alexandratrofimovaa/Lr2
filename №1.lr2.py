from csv import reader

def count_long_titles(): #функция подсчета книг с названием длинее 30 символов
    with open('books.csv', 'r') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
        c = 0
        for row in table:
            if len(row[1]) > 30: #длина названия
                c += 1
    return c

print(count_long_titles())
