'''
Написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её, 
читать список заметок, редактировать заметку, удалять заметку.
Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с 
запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска 
программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на 
усмотрение студента.
'''

import json
import datetime

notes = {}

def load():
    with open("Notes.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
        print("Выгрузка заметок произведена")
    return notes
    
def save():
    with open("Notes.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(notes, ensure_ascii=False))
                            

def add():
    print("Что будем добавлять?" '\n' "1 - новую заметку" '\n' "2 - заголовок" '\n' "3 - информацию в имеющуюся заметку")
    n = int(input("Введите число: "))
    if n == 1:
        number = input("Введите номер заметки: ")
        name = input("Введите заголовок: ")
        new_notes = input("Введите текст: ")
        dt_now = datetime.datetime.today()
        notes.update({number: {"заголовок": [name], "текст": [new_notes], "дата": dt_now.strftime('%d-%m-%Y %H:%M')}})
        print("Заметка создана")
        print(number, notes[number])
        save()
    if n == 2:
        number = input("Введите номер заметки: ")
        if number in notes:
            info = input("Введите новый заголовок: ")
            dt_now = datetime.datetime.today()
            notes[number]['заголовок'].append(info)
            notes[number]['дата'] = dt_now.strftime('%d-%m-%Y %H:%M')
            print(number, notes[number])
            save()
        else:
            print("Такой заметки не найдено!") 
    if n == 3:       
        number = input("Введите номер заметки: ")    
        if number in notes:
            info = input("Введите новую информацию: ")
            dt_now = datetime.datetime.today()
            notes[number]['текст'].append(info)
            notes[number]['дата'] = dt_now.strftime('%d-%m-%Y %H:%M')
            print(number, notes[number])
            save()
        else:
            print("Такой заметки не найдено!")     
    return notes

def change():
    print("Что будем менять? 1 - заголовок, 2 - текст")
    n = int(input("Введите число: "))
    if n == 1:
        number = input("Введите номер заметки: ")
        if number in notes:
            new_name = input("Введите новый заголовок: ")
            dt_now = datetime.datetime.today()
            notes[number]['заголовок'] = [new_name]
            notes[number]['дата'] = dt_now.strftime('%d-%m-%Y %H:%M')
            print(number, notes[number])
            save()
        else:
            print("Такой заметки не найдено!") 
    if n == 2:
        number = input("Введите номер заметки: ")
        if number in notes:
            new_text = input("Введите новый текст: ")
            dt_now = datetime.datetime.today()
            notes[number]['текст'] = [new_text]
            notes[number]['дата'] = dt_now.strftime('%d-%m-%Y %H:%M')
            print(number, notes[number])
            save()
        else:
            print("Такой заметки не найдено!") 
    

def delite():
    print("Что будем удалять? 1 - заметку, 2 - заголовок, 3 - текст")
    n = int(input("Введите число: "))
    if n == 1:
        number = input("Введите номер заметки: ")
        if number in notes:
            dt_now = datetime.datetime.today()
            del notes[number]
            print("Заметка удалена", dt_now.strftime('%d-%m-%Y %H:%M'))
            save() 
    if n == 2:
        number = input("Введите номер заметки: ")
        if number in notes:
            dt_now = datetime.datetime.today()
            notes[number]['заголовок'] = []
            notes[number]['дата'] = dt_now.strftime('%d-%m-%Y %H:%M')
            print(number, notes[number])
            save()
        else:
            print("Такой заметки не найдено!") 
    if n == 3:
        number = input("Введите номер заметки: ")
        if number in notes:
            dt_now = datetime.datetime.today()
            notes[number]['текст'] = []
            notes[number]['дата'] = dt_now.strftime('%d-%m-%Y %H:%M')
            print(number, notes[number])
            save()
        else:
            print("Такой заметки нет!") 
    return notes


while True:
    print()
    command = input("Команды: \n /load - выгрузка всех заметок \n /save - сохранение заметки \n /add - добавить заметку, текст \n /all - посмотреть все заметки \n /change - изменение данных \n /del - удаление данных \n Введите команду: ")
    if command == "/load":
        notes = load()
    if command == "/save":
        save()
    if command == "/add":
        add()
    if command == "/all":
        print("Список всех контактов:")
        print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in notes.items()) + "}")
    if command == "/change":
        change()
    if command == "/del":
        delite()
   