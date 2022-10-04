from dataclasses import field


def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def read_csv(filename: str) -> list: # чтение
    data = []
    fields = ['Фамилия','Имя', 'Телефон', 'Описание']
    with open(filename, 'w', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data

def find_by_name(data: list, last_name: str) -> str: # поиск по фамилии
    for el in data:
        if el.get('Фамилия') == last_name:
            return el.get('Телефон')
    return 'Такой абонент отсутствует'

def find_by_number(data: list, phone_number: str) -> str: # поиск по номеру
    for el in data:
        if el.get('Телефон') == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return 'Такой абонент отсутствует'