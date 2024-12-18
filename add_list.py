created_date = (input('Введите дату создания заметки в формате "день-месяц-год": '))
issue_date = (input('Введите дату истечения срока заметки в формате "день-месяц-год: '))
created_date_1 = (created_date[0:5]) #сокращенная дата до д-м без года
issue_date_1 = (issue_date[0:5])
username = input('Введите имя пользователя: ')
title1 = input('Введите заголовок заметки: ')
additional_title2 = int(input('Добавить дополнительный заголовок? (Если да, то введите "1", если нет, то "0"): '))
if additional_title2 == 1:
   additional_title_new2 = input('Введите дополнительный заголовок: ')
   additional_title3 = int(input('Добавить дополнительный заголовок? (Если да, то введите "1", если нет, то "0"): '))
   if additional_title3 == 1:
       additional_title_new3 = input('Введите дополнительный заголовок: ')
       if additional_title3 == 0:
           print("Продолжение создания заметки")
titles = [title1]
if additional_title2 == 1:
        titles.append(additional_title_new2)
        if additional_title3 == 1:
            titles.append(additional_title_new3)
            if additional_title3 == 0:
                print('Продолжение ввода данных')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки (например, "Активна", "Выполнена" или "В работе": ')

print('Имя пользователя:', username)
if additional_title2 == 1:
    print('Первый заголовок:', title1)
    print('Второй заголовок: ', additional_title_new2)
    if additional_title3 == 1:
        print('Третий заголовок: ', additional_title_new3)
else:
    print('Заголовок заметки: ', title1)
print('Описание заметки:', content)
print('Статус:', status)
(print('Дата создания заметки: ', created_date_1))
print('Дата истечения срока заметки: ', issue_date_1)
print(titles)

