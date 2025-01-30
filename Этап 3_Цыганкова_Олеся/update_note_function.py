from datetime import datetime

# Функция для проверки корректности формата даты
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%d-%m-%Y')
    except ValueError:
        return None

notes = []
# Функция обновления заметки
def update_note(note):
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
                note['Имя пользователя'] = new_value # Обновляем выбранное поле в заметке
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
                    try:  # проверка правильности ввода
                        new_status = int(new_status)
                    except ValueError:
                        print('Введено некорректное значение, пожалуйста, повторите попытку')
                        continue
                    if new_status == 1:
                        new_value = 'выполнено'  # переменная принимает новые значения в зависимости от выбора пользователя
                        print('Статус успешно обновлен на: ', new_status)
                        note['Статус'] = new_value # Обновляем выбранное поле в заметке
                    elif new_status == 2:
                        new_value = 'в процессе'
                        print('Статус успешно обновлен на: ', new_status)
                        note['Статус'] = new_value
                    elif new_status == 3:
                        new_value = 'отложено'
                        print('Статус успешно обновлен на: ', new_status)
                        note['Статус'] = new_value
                    elif new_status != 1 or new_status != 2 or new_status != 3:
                        print('Пожалуйста, введите корректное значение (от 1 до 3)')
            elif field_to_update == 5:
                while True:
                    new_value = input('Введите новый дедлайн (в формате: день-месяц-год): ')
                    validated_date = validate_date(new_value)
                    if validated_date:
                        new_value = validated_date.strftime("%d-%m-%Y")  # Преобразуем в нужный формат
                        note['Дедлайн'] = new_value # Обновляем выбранное поле в заметке
                        break
                    else:
                        print("Ошибка! Неверный формат даты. Используйте формат день-месяц-год, например, 30-11-2024.")
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

# Пример использования функции
if __name__ == "__main__":
    # Пример заметки
    note = {
        'Имя пользователя': 'Алексей',
        'Заголовок': 'Список покупок',
        'Описание': 'Купить продукты на неделю',
        'Статус': 'новая',
        'Дата создания': '27-11-2024',
        'Дедлайн': '30-11-2024'
    }
    notes.append(note)

    # Вызов функции обновления заметки
    updated_note = update_note(note)