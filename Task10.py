# 10. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.


finp = open('file.txt', 'w') # создали файл

while True:
    s = input()
    if s == '':
        break
    finp.write(s + '\n')
finp.close()

finp = open('file.txt', 'r') # количество строк
count = 0
for line in finp:
    count += 1
    print(len(line))
    print(len(line.split()))

print(f'Количество строк в файле: {count}')
finp.close()