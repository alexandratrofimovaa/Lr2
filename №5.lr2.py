from csv import reader

def find_tags(): #функция для поиска всех уникальных тэгов
    with open('books.csv', 'r') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
        tags = []
        for row in table:
            tag = row[12].split('#')
            for t in tag:
                if t not in tags and t != '':
                    tags.append(t)
    return tags

print(find_tags())