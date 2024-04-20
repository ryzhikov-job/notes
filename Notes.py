import json
import datetime


def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": str(datetime.datetime.now().timestamp()),
        "title": title,
        "body": body,
        "date": str(datetime.datetime.now())
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата создания: {note['date']}")
        print()


def delete_note():
    note_id = input("Введите ID заметки для удаления: ")
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")


def edit_note():
    note_id = input("Введите ID заметки для редактирования: ")
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note["title"] = title
            note["body"] = body
            note["date"] = str(datetime.datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")


def filter_notes_by_date():
    date_str = input("Введите дату в формате YYYY-MM-DD для фильтрации заметок: ")
    try:
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        notes = load_notes()
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note["date"], "%Y-%m-%d %H:%M:%S.%f") == target_date]
        if filtered_notes:
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print(f"Дата создания: {note['date']}")
                print()
        else:
            print("Заметок на указанную дату не найдено.")
    except ValueError:
        print("Неверный формат даты.")


def main():
    while True:
        print("Доступные команды:")
        print("1. Добавить заметку")
        print("2. Просмотреть все заметки")
        print("3. Удалить заметку")
        print("4. Редактировать заметку")
        print("5. Фильтровать заметки по дате")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "6":
            break
        else:
            print("Неверная команда. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
