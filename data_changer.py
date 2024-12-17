from datetime import datetime
created_date = input('Введите дату создания заметки в формате день-месяц-год: ')
issue_date = input('Введите дату истечения срока заметки в формате день-месяц-год: ')
created_date_obj = datetime.strptime(created_date, '%d-%m-%Y')
issue_date_obj = datetime.strptime(issue_date, '%d-%m-%Y')

print('Дата создания заметки:',created_date_obj.day,'-',created_date_obj.month)
print('Дата истечения срока заметки:', issue_date_obj.day,'-',issue_date_obj.month)
