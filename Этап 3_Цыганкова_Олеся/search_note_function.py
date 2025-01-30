def display_notes(notes):
    # Отображает список заметок в структурированном формате
    if not notes:
        print('У вас нет сохранённых заметок.')
        return

    print('Список заметок:')
    for i, note in enumerate(notes, start=1):
        print('------------------------------')
        print(f'Заметка №{i}:')
        print(f'Имя пользователя: {note.get('username', 'Не указано')}')
        print(f'Заголовок: {note.get('title', 'Без заголовка')}')
        print(f'Описание: {note.get('description', 'Без описания')}')
        print(f'Статус: {note.get('status', 'Не указан')}')
        print(f'Дата создания: {note.get('created_date', 'Не указана')}')
        print(f'Дедлайн: {note.get('issue_date', 'Не указан')}')

    print('------------------------------')

def search_notes(notes, keyword = None, status = None):
    found_notes = []
    if not notes:
        print('Список заметок пустой')
        return
    # Поиск по ключевому слову и статусу:
    if keyword and status:
        for i in notes:
            if (keyword.lower() in i.get('title').lower() or keyword.lower() in i.get('content').lower() or
            keyword.lower() in i.get('username').lower()) and status.lower() in i.get('status').lower():
                found_notes.append(i)
    # Поиск по ключевому слову:
    elif keyword:
        for i in notes:
            if (keyword.lower() in i.get('title').lower() or keyword.lower() in i.get('content').lower() or
            keyword.lower() in i.get('username').lower()):
                found_notes.append(i)
    # Поиск по статусу:
    elif status:
        for i in notes:
            if status.lower() in i.get('status').lower():
                found_notes.append(i)
    else:
        print('Критерий не указан')
        return
    return found_notes

# Заранее подготовленный список заметок:
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]
print(notes)
if notes:
    # Запрос критерия:
    while True:
        found_notes = []
        search_what = input('''По какому критерию искать заметки?
1. Ключевые слова
2. Статус
3. Ключевые слова и статус
Ваш выбор (введите номер от 1 до 3): ''')
        # Поиск по ключевым словам:
        if search_what == '1' or search_what.lower() == 'ключевые слова':
            keyword = input('Введите ключевое слово: ')
            found_notes = search_notes(notes, keyword=keyword)
            break
        # Поиск по статусу:
        elif search_what == '2' or search_what.lower() == 'статус':
            status = input('Введите статус заметки: ')
            found_notes = search_notes(notes, status=status)
            break
        # Поиск по ключевым словам и статусу:
        elif search_what == '3' or search_what.lower() == 'ключевые слова и статус':
            keyword = input('Введите ключевое слово: ')
            status = input('Введите статус: ')
            found_notes = search_notes(notes, keyword=keyword, status=status)
            break
        # Некорректный ввод:
        else:
            print('Некорректный ввод. Пожалуйста, повторите попытку.')
            continue
    if found_notes:
        display_notes(found_notes)
    else:
        print('Указанный ключ или статус не подходит ни одной заметке.')
else:
    print('Список заметок пуст.')
