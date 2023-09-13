import datetime

# Делаем глобальную переменную id, чтобы программа сама генерировала его при создании заметки
note_id_counter = 1

def open_create_file():
    data = open('заметки.txt', 'a')
    data.close()

def save_file():
    global note_id_counter  # обращаемся к глобальной переменной 
    title = input("Введите заголовок для заметки: ")
    body = input("Заметка: ")

    # создаём сегодняшнюю дату и время 
    current_datetime = datetime.datetime.now()
    date__notice = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # присваивыем id уникальный номер 
    id = note_id_counter
    note_id_counter += 1

    with open('заметки.txt', 'a', encoding='utf-8') as date:
        date.write(f"{id}; {title}; {body}; {date__notice}\n")
        print("Заметка сохранена.")

# функция для поиска заметки по заголовку
def find_notice():
    title = input("Введите заголовок заметки для поиска: ")
    with open('заметки.txt', 'r', encoding='utf-8') as date:
        notices = date.readlines()

    found = False
    for notice in notices:
        parts = notice.split(';')
        if len(parts) >= 2 and title.lower() == parts[1].strip().lower():
            print("Заметка найдена:")
            print("id:", parts[0])
            print("Заголовок:", parts[1])
            print("Заметка:", parts[2])
            print("Дата:", parts[3])
            found = True
            break

    if not found:
        print("Заметка не найдена")

# функция для изменения заметки по id
def edit_notice():
    id_to_edit = input("Введите id заметки для редактирования: ")
    new_data = input("Введите новую информацию: ")
    
    with open('заметки.txt', 'r', encoding='utf-8') as date:
        lines = date.readlines()

    found = False
    updated_lines = []
    for line in lines:
        parts = line.split(';')
        if len(parts) >= 1 and id_to_edit == parts[0].strip():
            updated_lines.append(f"{parts[0]}; {parts[1]}; {new_data}; {parts[3]}")
            found = True
        else:
            updated_lines.append(line)

    if found:
        with open('заметки.txt', 'w', encoding='utf-8') as date:
            date.writelines(updated_lines)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка не найдена.")

# функция для удаления записки по id
def delete_notice():
    id_to_delete = input("Введите id заметки для удаления: ")
    with open('заметки.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found = False
    updated_lines = []
    for line in lines:
        parts = line.split(';')
        if len(parts) >= 1 and id_to_delete == parts[0].strip():
            found = True
        else:
            updated_lines.append(line)

    if found:
        with open('заметки.txt', 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")

# для поиска заметки по дате
def find_notice_by_date():
    date_to_find = input("Введите дату (гггг-мм-дд): ")
    try:
        date_to_find = datetime.datetime.strptime(date_to_find, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Используйте гггг-мм-дд.")
        return

    with open('заметки.txt', 'r', encoding='utf-8') as date:
        notices = date.readlines()

    found = False
    for notice in notices:
        parts = notice.split(';')
        if len(parts) >= 4:
            notice_date = datetime.datetime.strptime(parts[3].strip(), "%Y-%m-%d %H:%M:%S")
            if date_to_find.date() == notice_date.date():
                print("Заметка найдена:")
                print("id:", parts[0])
                print("Заголовок:", parts[1])
                print("Заметка:", parts[2])
                print("Дата:", parts[3])
                found = True

    if not found:
        print("Заметки не найдены для указанной даты.")

# функция для рассмотрения всего файла
def display_file_contents():
    with open('заметки.txt', 'r', encoding='utf-8') as date:
        contents = date.read()
        if contents:
            print("Содержимое файла:")
            print(contents)
        else:
            print("Файл пуст.")

def main():
    while True:
        print("Книга заметок:")
        print("1. создать файл")
        print("2. Сохранить заметку")
        print("3. Найти заметку")
        print("4. Изменить заметку")
        print("5. Удалить заметку")
        print("6. Показать содержимое файла")
        print("7. Найти заметки по дате")
        print("8. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            open_create_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            find_notice()
        elif choice == "4":
            edit_notice()
        elif choice == "5":
            delete_notice()
        elif choice == "6":
            display_file_contents()
        elif choice == "7":
            find_notice_by_date()    
        elif choice == "8":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Повторите попытку.")
            
if __name__ == "__main__":
    main()
