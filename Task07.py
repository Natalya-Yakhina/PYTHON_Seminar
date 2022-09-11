# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой

# string1 = 'I love apples'
# string2 = 'apples'
# if len(string1) > len(string2):
#     print(string1.count(string2))  
# else:
#      print(string2.count(string1))


a = 'pyt' # решение с перебором
b = 'pythonpythonpython'
count = 0
for i in range(0, len(b) - len(a)):
    if b[i:i + len(a)] == a:
        count += 1 
print(count)