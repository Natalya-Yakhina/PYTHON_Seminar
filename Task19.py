# НОД

# ============== с рекурсией ================
# import math
# print(math.gcd(a, b))

# def NOD(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return NOD(b, a % b)

# a = int(input())
# b = int(input())
# print(NOD(a, b))

# НОД2
a=20
b=58

if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b
print(a)
# НОД3
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)
# НОД4
c = gcd(a, b)