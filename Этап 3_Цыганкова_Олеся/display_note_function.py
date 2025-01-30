
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

# Тестовые данные
if __name__ == '__main__':
    # Список заметок
    test_notes = [
        {
            'username': 'Алексей',
            'title': 'Список покупок',
            'description': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024',
        },
        {
            'username': 'Мария',
            'title': 'Учеба',
            'description': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '25-11-2024',
            'issue_date': '01-12-2024',
        },
    ]

    # Пустой список заметок
    empty_notes = []

    print('Пример 1: Пустой список заметок')
    display_notes(empty_notes)

    print('\nПример 2: Список с несколькими заметками')
    display_notes(test_notes)