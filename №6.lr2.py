from csv import reader


def spis_pop(): #создание списка 20 самых популярных книг
    with open('books.csv', 'r') as csvfile:
        table = list(reader(csvfile, delimiter=';'))[1:]
        popularity = {}
        for row in table:
            book = (row[1], row[3])
            popularity[book] = popularity.get(book, 0) + int(row[8]) 
    spis_pop = sorted(popularity.items(), key=lambda item: item[1], reverse=True)
    for (title, author), count in spis_pop[:20]:
        print(title, ',', author, '-', count)


spis_pop()