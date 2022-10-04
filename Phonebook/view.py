from numpy import record

def show_menu(): # вывод меню на экран
    print("\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти по фамилии\n"
        "3. Найти по номеру\n"
        "4. Добавить в справочник\n"
        "5. Сохранить справочник в текстовом формате\n"
        "6. Закончить работу\n")
    choice = int(input())
    return choice

def print_result(data: list): # вывод результата на экран
    for el in data:
        s = '' # разбиваем словарь на элементы
        for v, k in el.items(): # items - из словаря берет сразу два значения
            s += f'{v}: {k}\n'
        print(s)

def get_search_name() -> str:
    return input('Введите фамилию для поиска')

def get_search_number() -> str:
    return input('Введите номер телефона для поиска')

def get_new_user() -> str: # запись нового элемента
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Введите описание: ')
    return f'{last_name, {first_name}, {phone_number}, {description}}'

def get_file_name() -> str:
    return input('Введите название файла для сохранения: ')

def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get('Фамилия') == last_name:
            return el.get('Телефон')
    return 'Такой абонент отсутствует'

def find_by_number(data: list, last_name: str) -> str:
    for el in data:
        if el.get('Телефон') == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return 'Такой абонент отсутствует'

def add_user(data: list, last_name: str):
    fields = ["Фамилия", "Имя", "Номер", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)