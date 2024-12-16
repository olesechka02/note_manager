from datetime import datetime

created_date = (input('Введите дату создания заметки в формате "день-месяц-год": '))
issue_date = (input('Введите дату истечения срока заметки в формате "день-месяц-год: '))
created_date_1 = (str(created_date[0:5])) #сокращенная дата до д-м без года
issue_date_1 = (str(issue_date[0:5]))

username = input('Введите имя пользователя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки (например, "Активна", "Выполнена" или "В работе": ')

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус:', status)
print('Дата создания заметки: ' + created_date_1)
print('Дата истечения срока заметки: ' + issue_date_1)

