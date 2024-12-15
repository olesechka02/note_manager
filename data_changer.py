created_date = '11-12-2024'
temp_created_date = '11-12'
print('Дата создания заметки:', temp_created_date)
issue_date = '30-12-2024'
temp_issue_date = '30-12'
print('Дата истечения заметки:', temp_issue_date)

#Нашла еще такой способ:

import datetime
dc = datetime.date(2024, 12, 11) # dc - это created_date
print('Дата создания заметки:', dc.day,'-',dc.month)
di = datetime.date(2024, 12, 30) #di - это issue_date
print('Дата истечения заметки:', di.day,'-',di.month)
