def expp(last_name):
    with open('database.csv.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for persone in info_list:
            if last_name in persone:
                print(persone)
