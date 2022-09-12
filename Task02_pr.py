# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

# A = [1, 3, 5, 7, 9]
# sum = 0
# poz_min = 0
# poz_max = 0
# size = len(A)
# i = 1

# while i < size:
#     if A[i] > A[poz_max]:
#         poz_max = i
#     elif A[i] < A[poz_min]:
#         poz_min = i
#     i =+ 1
# print(poz_max, poz_min)


A = [1, 2, 3, 8, 9, 10]
sum = 0
poz_min = 0
poz_max = 0
i = 1
size = len(A)
while i < size:
    if A[i] > A[poz_max]:
        poz_max = i
    elif A[i] < A[poz_min]:
        poz_min = i
    i += 1
print(poz_min, poz_max)
if poz_max > poz_min:
    for i in range(poz_min, poz_max+1):
        sum = sum + A[i]
elif poz_max < poz_min:
    for i in range(poz_max, poz_min+1):
        sum = sum + A[i]
    else:
        sum = A[poz_max]
print(A, sum)