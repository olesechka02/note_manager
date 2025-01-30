from datetime import datetime

notes = [
    {
        'Имя пользователя': 'Алексей',
        'Заголовок': 'Список покупок',
        'Описание': 'Купить продукты на неделю',
        'Статус': 'новая',
        'Дата создания': '27-11-2024',
        'Дедлайн': '30-11-2024',
    },
    {
        'Имя пользователя': 'Мария',
        'Заголовок': 'Учеба',
        'Описание': 'Подготовиться к экзамену',
        'Статус': 'в процессе',
        'Дата создания': '25-11-2024',
        'Дедлайн': '01-12-2024',
    }]

def validate_date(date_str):  # Проверка формата даты
    try:
        return datetime.strptime(date_str, '%d-%m-%Y')
    except ValueError:
        return None

def create_note():
    username = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    description = input('Введите описание заметки: ')

    while True:
        status = input('Введите статус заметки (новая, в процессе, выполнена): ').lower()
        if status in ['новая', 'в процессе', 'выполнена']:
            break
        print('Неверный статус! Выберите один из вариантов: новая, в процессе, выполнена.')

    while True:
        issue_date_str = input('Введите дату дедлайна (день-месяц-год): ')
        issue_date = validate_date(issue_date_str)
        if issue_date:
            break
        print('Неверный формат даты! Используйте формат день-месяц-год, например, 30-01-2025.')

    created_date = datetime.now().strftime('%d-%m-%Y')
    note = {
        'Имя пользователя': username,
        'Заголовок': title,
        'Описание': description,
        'Статус': status,
        'Дата создания': created_date,
        'Дедлайн': issue_date.strftime('%d-%m-%Y')
    }
    notes.append(note)
    print('Заметка успешно создана:', note)

def display_notes(notes):
    if not notes:
        print('У вас нет сохранённых заметок.')
        return
    print('Список заметок:')
    for i, note in enumerate(notes, start=1):
        print(f'\nЗаметка №{i}:')
        print(f'Имя пользователя: {note.get("Имя пользователя", "Не указано")}')
        print(f'Заголовок: {note.get("Заголовок", "Без заголовка")}')
        print(f'Описание: {note.get("Описание", "Без описания")}')
        print(f'Статус: {note.get("Статус", "Не указан")}')
        print(f'Дата создания: {note.get("Дата создания", "Не указана")}')
        print(f'Дедлайн: {note.get("Дедлайн", "Не указан")}')

def update_note():
    display_notes(notes)
    try:
        note_index = int(input('Введите номер заметки для обновления: ')) - 1
        if note_index < 0 or note_index >= len(notes):
            print('Неверный номер заметки.')
            return
        note = notes[note_index]
        print('\nТекущие данные заметки:')
        for i in range(len(notes)):
            print(f'\nЗаметка № {i + 1}: ')
            for key, value in notes[i].items():
                print(key, '-', value)
        print()
        while True:
            # Запрашиваем, какое поле пользователь хочет обновить
            print('Какие данные вы хотите обновить?:',
                  '1. Имя пользователя',
                  '2. Заголовок',
                  '3. Описание',
                  '4. Статус',
                  '5. Дедлайн',
                  sep='\n')
            field_to_update = input('Ваш выбор (выберите цифру от 1 до 5): ')
            try:  # проверка правильности ввода
                field_to_update = int(field_to_update)
            except ValueError:
                print('Введено некорректное значение, пожалуйста, повторите попытку')
                continue
            if field_to_update in range(1, 6):
                if field_to_update == 1:
                    new_value = input('Введите новое значение для "Имя пользователя": ')
                    note['Имя пользователя'] = new_value  # Обновляем выбранное поле в заметке
                elif field_to_update == 2:
                    new_value = input('Введите новое значение для "Заголовок": ')
                    note['Заголовок'] = new_value
                elif field_to_update == 3:
                    new_value = input('Введите новое значение для "Описание": ')
                    note['Описание'] = new_value
                elif field_to_update == 4:
                    while True:
                        print('Выберите новый статус заметки:',
                              '1. выполнено',
                              '2. в процессе',
                              '3. отложено',
                              sep='\n')  # красивенький вывод вариантов статуса
                        new_status = input('Ваш выбор: ')
                        if new_status == '1':
                            new_value = 'выполнено'  # переменная принимает новые значения в зависимости от выбора пользователя
                            print('Статус успешно обновлен на: ', new_status)
                            note['Статус'] = new_value  # Обновляем выбранное поле в заметке
                            break
                        elif new_status == '2':
                            new_value = 'в процессе'
                            print('Статус успешно обновлен на: ', new_status)
                            note['Статус'] = new_value
                            break
                        elif new_status == '3':
                            new_value = 'отложено'
                            print('Статус успешно обновлен на: ', new_status)
                            note['Статус'] = new_value
                            break
                        else:
                            print('Пожалуйста, введите корректное значение (от 1 до 3)')
                            continue
                elif field_to_update == 5:
                    while True:
                        new_value = input('Введите новый дедлайн (в формате: день-месяц-год): ')
                        validated_date = validate_date(new_value)
                        if validated_date:
                            new_value = validated_date.strftime("%d-%m-%Y")  # Преобразуем в нужный формат
                            note['Дедлайн'] = new_value  # Обновляем выбранное поле в заметке
                            break
                        else:
                            print(
                                "Ошибка! Неверный формат даты. Используйте формат день-месяц-год, например, 30-11-2024.")
            else:
                print('Пожалуйста, введите корректное значение (от 1 до 5).')
            break
        # Возвращаем обновлённую заметку
        print("\nЗаметка обновлена:")
        for i in range(len(notes)):
            print(f'\nЗаметка № {i + 1}: ')
            for key, value in notes[i].items():
                print(key, '-', value)
        return note
    except ValueError:
        print('Ошибка! Введите корректный номер заметки.')

def delete_note():
    display_notes(notes)
    try:
        note_index = int(input('Введите номер заметки для удаления: ')) - 1
        if note_index < 0 or note_index >= len(notes):
            print('Неверный номер заметки.')
            return
        deleted_note = notes.pop(note_index)
        print('Заметка удалена:', deleted_note)
    except ValueError:
        print('Ошибка! Введите корректный номер заметки.')

def search_notes(notes, keyword = None, status = None):
    found_notes = []
    if not notes:
        print('Список заметок пустой')
        return
    # Поиск по ключевому слову и статусу:
    if keyword and status:
        for i in notes:
            if (keyword.lower() in i.get('Заголовок').lower() or keyword.lower() in i.get('Описание').lower() or
                keyword.lower() in i.get('Имя пользователя').lower()) and status.lower() in i.get('Статус').lower():
                found_notes.append(i)
    # Поиск по ключевому слову:
    elif keyword:
        for i in notes:
            if (keyword.lower() in i.get('Заголовок').lower() or keyword.lower() in i.get('Описание').lower() or
                    keyword.lower() in i.get('Имя пользователя').lower()):
                found_notes.append(i)
    # Поиск по статусу:
    elif status:
        for i in notes:
            if status.lower() in i.get('Статус').lower():
                found_notes.append(i)
    else:
        print('Критерий не указан')
        return
    return found_notes

def main_menu():
    while True:
        print('\nМеню действий:',
              '1. Создать новую заметку',
              '2. Показать все заметки',
              '3. Обновить заметку',
              '4. Удалить заметку',
              '5. Найти заметки',
              '6. Выйти из программы',
              sep='\n')

        choice = input('Ваш выбор: ')
        if choice == '1':
            create_note()
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes(notes, keyword = None, status = None)
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
        elif choice == '6':
            print('Программа завершена.')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')

if __name__ == '__main__':
    main_menu()
