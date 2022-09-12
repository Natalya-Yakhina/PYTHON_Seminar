# 5. Напишите программу, которая принимает на вход число и проверяет 
# кратно ли оно 5 и 10 или 15 но не 30

# x = int(input("Введите число: "))

# if ((x % 5 ==0) and (x % 10 == 0) or x % 15 == 0) and not (x % 30 == 0):
#     print("ратно")
# else:
#     print("нет")


def input_numbers(input_text): # функция проверки на ввод числа
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
                print("Ошибка! Это не число!")
    return number

num = input_numbers("Введите число: ")