



import json
import os
import datetime


FILENAME = 'BASE.json'






def load_notes():
    
    if os.path.isfile(FILENAME):
        with open(FILENAME, 'r') as f:
            notes = json.load(f)
    else:
        notes = []
    return notes


def save_notes(notes):
    with open(FILENAME, 'w') as f:
        json.dump(notes, f, indent=4)


def create_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'id': len(notes)+1, 'title': title, 'body': body, 'data': now}
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно создана')
    
     
    



def read_notes():
    if not notes:
        print('Не найдено.')
    else:
        for note in notes:
            print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Дата создания: {note["data"]}')


def edit_note():
    id = int(input('Введите ID заметки: '))
    note = next((n for n in notes if n['id'] == id), None)
    if note:
        note['title'] = input('Измените заголовок: ') or note['title']
        note['body'] = input('Измените текст: ') or note['body']
        note['updated_at'] = datetime.datetime.now().isoformat()
        save_notes(notes)
        print('Заметка успешно изменена.')
    else:
        print(f'Заметка с этим ID {id} не найдена.')


def delete_note():
    id = int(input('Введите ID заметки для удален: '))
    note = next((n for n in notes if n['id'] == id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print('Заметка успешно удалена.')
    else:
        print(f'Заметка с этим ID  {id} не найдена.')


notes = load_notes()


while True:
    print('Команды:')
    print('1 - Создать заметку')
    print('2 - Просмотреть  все заметки')
    print('3 - Редактировать заметки')
    print('4 - Удалить заметку')
    print('0 - Выход')
    command = input()

    if command == '1':
        create_note()
    elif command == '2':
        read_notes()
    elif command == '3':
        edit_note()
    elif command == '4':
        delete_note()
    elif command == '0':
        break
    else:
        print('Ошибка.')