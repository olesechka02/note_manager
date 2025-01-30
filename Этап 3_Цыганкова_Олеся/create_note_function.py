from datetime import datetime

def validate_date(date_str): # Функция для проверки формата даты
    try:
        return datetime.strptime(date_str, '%d-%m-%Y')
    except ValueError:
        return None

def create_note(): # Функция создания заметки
    # Запрос у пользователя данных для заметки
    username = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки: ')
    while True: # Запрос статуса с проверкой на корректность
        status = input('Введите статус заметки (новая, в процессе, выполнено): ').lower()
        if status in ['новая', 'в процессе', 'выполнена']:
            break
        else:
            print('Неверный статус! Выберите один из вариантов: "новая", "в процессе", "выполнена".')
    while True: # Запрос даты дедлайна с проверкой на правильный формат
        issue_date_str = input('Введите дату дедлайна (день-месяц-год): ')
        issue_date = validate_date(issue_date_str)
        if issue_date:
            break
        else:
            print('Неверный формат даты! Используйте формат день-месяц-год, например, 30-01-2025.')
    created_date = datetime.now().strftime('%d-%m-%Y') # Получение текущей даты
    # Формирование словаря с данными заметки
    note = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date.strftime('%d-%m-%Y')
    }
    return note
notes = [] # Формирование списка словарей для хранения нескольких заметок
# Вызов функции и вывод результата
if __name__ == '__main__':
    note = create_note()
    print('Заметка создана:', note)
    notes.append(note)