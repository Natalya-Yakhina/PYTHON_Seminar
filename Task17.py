# 17. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

from random import randint


a = int(input('Введите число: '))
list = []

for i in range(a):
    f = randint(-a, a)
    list.append(f)
print(list)
# print(min(list))
# print(max(list))



print(f'Наименьшее число: {min(list)}, наибольшее число: {max(list)}')