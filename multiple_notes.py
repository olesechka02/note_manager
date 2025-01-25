from datetime import datetime, date
print('Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.')
notes = []
note = {}
titles_list = []
def user_name():
    while new_note.strip() == '+':
        note['Имя пользователя'] = input('Введите имя пользователя: ')
        if note['Имя пользователя'].strip() == '':  # проверка пустого ввода и удаление начальных/конечных пробелов
            print('Имя пользователя не может быть пустым, пожалуйста, повторите ввод.')
        else:
            break  # выход из цикла
def title():
    while new_note.strip() == '+':
        title1 = input('Введите заголовок заметки (или оставьте поле пустым для завершения): ')
        titles_list.append(title1)
        note['Заголовок заметки'] = title1
        if title1 == '':
            break
        if title1 not in '':
            additional_title = input('Введите заголовок заметки (или оставьте поле пустым для завершения): ')
            if additional_title not in '':
                titles_list.append(additional_title)
                note['Дополнительный заголовок'] = additional_title
            if additional_title == '':
                break
def content():
    while new_note.strip() == '+':
        note['Описание заметки'] = input('Введите описание заметки: ')
        if note['Описание заметки'].strip() == '':  # проверка пустого ввода и удаление начальных/конечных пробелов:
            print('Описание заметки не может быть пустым, пожалуйста, повторите ввод')
        else:
            break
def status():
    while new_note.strip() == '+':
        print('Выберите статус заметки:',
              '1. выполнено',
              '2. в процессе',
              '3. отложено',
              sep='\n')  # красивенький вывод вариантов статуса
        status = input('Ваш выбор: ')
        try:  # проверка правильности ввода
            status = int(status)
        except ValueError:
            print('Введено некорректное значение, пожалуйста, повторите попытку')
            continue
        if status == 1:
            status1 = 'выполнено'  # переменная принимает новые значения в зависимости от выбора пользователя
            note['Статус заметки'] = status1
            break
        elif status == 2:
            status2 = 'в процессе'
            note['Статус заметки'] = status2
            break
        elif status == 3:
            status3 = 'отложено'
            note['Статус заметки'] = status3
            break
        elif status != 1 or status != 2 or status != 3:
            print('Пожалуйста, введите корректное значение (от 1 до 3)')
            continue
        break
def day_today():
    if new_note.strip() == '+':
        current_date = date.today()
        today = current_date.strftime('%d-%m-%Y')
        note['Дата создания заметки'] = today
        print('Дата создания заметки: ', today)
def deadline():
    while new_note.strip() == '+':
        issue_date_str = input('Введите дедлайн (в формате день-месяц-год): ')
        try:
            datetime.strptime(issue_date_str, '%d-%m-%Y')
            break
        except ValueError:
            print(f'Неправильный формат даты {issue_date_str}')
        note['Дедлайн'] = issue_date_str
while True:
    new_note = input('Создать новую заметку? ("+" - Да, другой символ или пустой ввод - Нет): ')
    if new_note == '+':
        user_name()
        title()
        content()
        status()
        day_today()
        deadline()
        notes.append(note)
    else:
        print('Ввод заметок завершен.')
        break
    print('\nСписок заметок:')
    for i in range(len(notes)):
        print(f'\nЗаметка № {i + 1}: ')
        for key, value in notes[i].items():
            print(key, '-', value)