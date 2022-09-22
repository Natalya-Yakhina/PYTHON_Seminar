# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

# inp = list(map(str, input('Введите список: ').split()))
# print([int(num) for num in filter(lambda num: num.isnumeric(), inp)]) # isnumeric возвращает числа

# ====================================================================================================

a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
 
b= filter(str.isalpha, a) # isalpha ищет буквы
c= filter(str.isdigit, a) # isdigit ищет числа

print(*b)
print(*c)