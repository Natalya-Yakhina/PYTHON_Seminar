def impo(some_persone):
    with open('info.txt', 'a', encoding='utf-8') as f:
        f.write(some_persone + '\n')