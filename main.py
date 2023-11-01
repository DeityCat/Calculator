from colorama import init
from colorama import Fore, Back, Style

init()

print( Fore.WHITE )
print( Back.BLUE )
print('Калькулятор v1.0')

print( Fore.WHITE )
print( Back.GREEN )

nameOfOperation = input('Введите операцию (+, -, *, /): ')
sumOfNumbers = input('Введите кол-во чисел для счисления (2, 3): ')

# Сложение
if sumOfNumbers == '2' and nameOfOperation == '+':
    a = int(input('Введите первое слагаемое: '))
    b = int(input('Введите второе слагаемое: '))
    c = a + b
    print('Результат (сумма): ' + str(c))
elif sumOfNumbers == '3' and nameOfOperation == '+':
    a = int(input('Введите первое слагаемое: '))
    b = int(input('Введите второе слагаемое: '))
    c = a + b
    print('Промежуточный результат: ' + str(c))
    doubleAction = input('Выберите второе действие (+, -, *, /): ')
    if doubleAction == '+':
        d = int(input('Введите третье слагаемое: '))
        e = c + d
    elif doubleAction == '-':
        d = int(input('Введите третье значение: '))
        e = c - d
    elif doubleAction == '*':
        d = int(input('Введите третье значение: '))
        e = c * d   
    elif doubleAction == '/':
        d = int(input('Введите третье значение: '))
        e = c / d
    else:
        print('Введена неправильная или несуществующая команда!')
    print('Результат счисления: ' + str(e)) 

#Вычитание
if sumOfNumbers == '2' and nameOfOperation == '-':
    a = int(input('Введите уменьшаемое: '))
    b = int(input('Введите вычитаемое: '))
    c = a - b
    print('Результат (разность): ' + str(c))
elif sumOfNumbers == '3' and nameOfOperation == '-':
    a = int(input('Введите уменьшаемое: '))
    b = int(input('Введите вычитаемое: '))
    c = a - b
    print('Промежуточный результат: ' + str(c))
    doubleAction = input('Выберите второе действие (+, -, *, /): ')
    if doubleAction == '+':
        d = int(input('Введите третье значение: '))
        e = c + d
    elif doubleAction == '-':
        d = int(input('Введите третье значение: '))
        e = c - d
    elif doubleAction == '*':
        d = int(input('Введите третье значение: '))
        e = c * d   
    elif doubleAction == '/':
        d = int(input('Введите третье значение: '))
        e = c / d
    else:
        print('Введена неправильная или несуществующая команда!')  
    print('Результат счисления: ' + str(e)) 

#Умножение
if sumOfNumbers == '2' and nameOfOperation == '*':
    a = int(input('Введите первый множитель: '))
    b = int(input('Введите второй множитель: '))
    c = a * b
    print('Результат (произведение): ' + str(c))
elif sumOfNumbers == '3' and nameOfOperation == '*':
    a = int(input('Введите первый множитель: '))
    b = int(input('Введите второй множитель: '))
    c = a * b
    print('Промежуточный результат: ' + str(c))
    doubleAction = input('Выберите второе действие (+, -, *, /): ')
    if doubleAction == '+':
        d = int(input('Введите третье значение: '))
        e = c + d
    elif doubleAction == '-':
        d = int(input('Введите третье значение: '))
        e = c - d
    elif doubleAction == '*':
        d = int(input('Введите третий множитель: '))
        e = c * d   
    elif doubleAction == '/':
        d = int(input('Введите третье значение: '))
        e = c / d
    else:
        print('Введена неправильная или несуществующая команда!') 
    print('Результат счисления: ' + str(e)) 

#Деление
if sumOfNumbers == '2' and nameOfOperation == '/':
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    c = a / b
    print('Результат (частное): ' + str(c))
elif sumOfNumbers == '3' and nameOfOperation == '/':
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    c = a / b
    print('Промежуточный результат: ' + str(c))
    doubleAction = input('Выберите второе действие (+, -, *, /): ')
    if doubleAction == '+':
        d = int(input('Введите третье слагаемое: '))
        e = c + d
    elif doubleAction == '-':
        d = int(input('Введите третье значение: '))
        e = c - d
    elif doubleAction == '*':
        d = int(input('Введите третье значение: '))
        e = c * d   
    elif doubleAction == '/':
        d = int(input('Введите третье значение: '))
        e = c / d
    else:
        print('Введена неправильная или несуществующая команда!') 
    print('Результат счисления: ' + str(e)) 

input()

        



















