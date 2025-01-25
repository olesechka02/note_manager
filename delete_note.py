# Функция вывода заметок
def show_notes(notes):
    if not notes:
        print('Список заметок пуст.')
        return
    print('Текущие заметки:')
    for index, note in enumerate(notes, 1):
        print(f'{index}. Имя: {note['username']}')
        print(f'  Заголовок: {note['title']}')
        print(f'  Описание: {note['content']}\n')

# Функция удаления заметки по имени пользователя или заголовку
def delete_note_by_criteria(notes, criteria):
    deleted = False
    for note in notes[:]:
        if criteria.lower() in note['username'].lower() or criteria.lower() in note['title'].lower():
            notes.remove(note)
            deleted = True
    return deleted

def main():
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену'}
    ]
    while True:
        show_notes(notes) # Показываем список заметок
        criteria = input('Введите имя пользователя или заголовок для удаления заметки: ').strip() # Запрашиваем критерий для удаления
        if delete_note_by_criteria(notes, criteria):  # Удаляем заметки по критерию
            print('Успешно удалено. Остались следующие заметки:')
            show_notes(notes)
        else:
            print('Заметок с таким именем пользователя или заголовком не найдено.')
        continue_choice = input('Хотите удалить еще заметку? (да/нет): ').strip().lower()  # Спрашиваем, хочет ли пользователь продолжить
        if continue_choice != 'да':
            print('До свидания!')
            break

main()