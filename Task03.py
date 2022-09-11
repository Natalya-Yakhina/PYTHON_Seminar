# 3. Напишите программу, которая будет принимать на вход число N и выводить числа от -N до N

# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

a = int(input("Введите число: "))
n = -a 
f = []

for i in range(a*2 + 1):
    f.append(int(n))
    n = n+1
print(f)

# N = int(input("Введите число: "))
# if N < 0:
#     N = -N
# ans = list(range(-N, N+1))
# print(ans)