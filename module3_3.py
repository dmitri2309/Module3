# функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params(a = 1, b = 'строка', c = True)
print_params()
print_params(b = 25, c = [1,2,3])

# распаковка параметров
value_list = [35,[4,5,6],False]
values_dict = {'a':1,'b':'строка','c':True}
print_params(*value_list)
print_params(**values_dict)

# распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)