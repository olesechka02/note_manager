print('Добро пожаловать в Менеджер заметок!')
# создаем переменную вне цикла, чтобы можно было потом ее добавить в список и с ней работать
titles = input('Введите заголовок заметки (или оставьте поле пустым для завершения): ')
titles_list = [titles]
while titles not in '':  # если заголовок пустой, то цикл не запускается
    title_again = input('Введите заголовок заметки (или оставьте поле пустым для завершения): ')
    titles_list.append(title_again)
    if title_again == '': # если пользователь ничего не вводит, то цикл завершается
        break
titles_list.remove('') # убираем пустые значения из списка
if titles == '': # проверка, есть ли заголовки вообще
    print('Заголовки отсутствуют')
else:
    print('Заголовки заметки: ')
    for i in titles_list: # вывод заголовков в читаемом виде
        print('-', i)