# НОД

# a = 66
# b = 55
# c = 0
# for i in range(min(a, b), 1, -1):
#     print(i)
#     if a % i == 0 and b % i == 0:
#         c = i
#         break
# print(c)

a = 66
b = 55
# c = 0
# for i in range(1, min(a, b)+1):
#     print(i)
#     if a % i == 0 and b % i == 0:
#         c = i

# print(c)

# def NOD(a, b): # с рекурсией
#     if a % b == 0:
#         return b
#     else:
#         return NOD(b, a % b)


# a = int(input())
# b = int(input())
# print(NOD(a, b))

# a=20
# b=58
# if a < b :
#     a, b = b, a
# while b!=0:
#     a, b = b, a % b
# print(a)

# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)

import math
print(math.gcd(a, b))