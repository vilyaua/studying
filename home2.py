'''
Написать функцию для распечатывания квадрата.
Принимает два параметра  n - размер квадрата и char - символ для печатания.
Пример:
»>print_square(4, "$")
$$$$
$$$$
$$$$
$$$$
'''

n = 5
ch = 'G'

def print_square(n, ch):
    rez = ch * n
    for i in range(n):
        print(rez)

print_square(n, ch)
