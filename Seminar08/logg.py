def log_info(info):
    with open('info.txt', 'a', encoding='utf-8') as f:
        if len(info.split()) == 1:
            f.write(f'Эскпорт - {info} + \n')
        else:
            f.write(f'Импорт - {info} + \n')

