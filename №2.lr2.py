from csv import reader


with open ('books.csv', 'r') as csvfile:
    table = list(reader(csvfile, delimiter=';'))


def find_string(searchline,string):
    string = string.lower() #заменяем все буквы на маленькие
    index = string.find(searchline) #ищем соответствие между тем, что вводят с клавиатуры и имеющимся значением
    return index


def search(table):
    searchline = input('Введите имя автора: ').strip() 
    matches = []
    for row in table:
        if row[0] == 'ID': #проверка на то, не является ли первый столбец заголовком
            continue
        if (find_string(searchline,row[4]) != -1 or find_string(searchline,row[3]) != -1) and float(row[7]) < 200:
            matches.append(row)
    return matches


results = search(table)
if results: #вывод результата
    for row in results:
        print(row)
else:
    print('Ничего не найдено')


