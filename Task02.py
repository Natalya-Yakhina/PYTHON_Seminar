# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# arr = [a, b, c, d, e]
# print(max(arr))

numbers = [1, 4, 8, 7, 5]
a = int(input("Введите кол-во чисел для сравнения - "))
numbers = []
for i in range(a):
    numbers.append(int(input()))
#print(max(numbers))
x = numbers[0]
for i in range(len(numbers)):
    if x < numbers[i]:
        x = numbers[i]
    print(x)