
from datetime import datetime
from datetime import date
# текущая дата
current_date = date.today()
today = current_date.strftime('%d-%m-%Y')
print('Текущая дата: ', today)

# проверка правильности ввода
while True:
    try:
        issue_date_str = input('Введите дату дедлайна (в формате день-месяц-год): ')
        datetime.strptime(issue_date_str, '%d-%m-%Y')
        break
    except ValueError:
        print(f'Неправильный формат даты: {issue_date_str}. Пожалуйста, введите дату в формате "день-месяц-год"')
# определяем время до дедлайна
deadline = datetime.strptime(issue_date_str, '%d-%m-%Y') # дедлайн в нужном формате
deadline = deadline.date() # дата дедлайна чтобы была только дата
delta = deadline - current_date # сколько времени прошло
day = delta.days # перевод разницы между дедлайном и текущей датой в дни
if day > 0:
    print(f'До дедлайна осталось {day} дн.')
elif day == 0:
    print('Внимание, дедлайн истекает сегодня!')
else:
    day = day * -1 # если дедлайн в прошлом времени, то делаем разницу дней со знаком +
    print(f'Дедлайн истек {day} дн. назад')
