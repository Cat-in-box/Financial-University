# -*- coding: utf-8 -*-
s = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
s_str = 'Белочка кушала орешек.'

#2
print('Длина коллекции', len(s), '\n')

#3
if 11 in s:
    print('Число', 11, 'есть в коллекции\n')
else:
    print('Числа', 11, 'нет в коллекции\n')
    
#4
print(s_str)
print('Строчка "куш" начинается в предложении с', s_str.find('куш'), 'символа\n')

#5
p = 1
for i in range (len(s)):
    p*=s[i]
print('Произведение всех элементов коллекции равно', p, '\n')

#6
print('Максимальный элемент коллекции', max(s))
print('Минимальный элемент коллекции', min(s))
print('Сумма всех элементов коллекции', sum(s), '\n')

#7
inp = input('Введите элемент, который хотите найти ')
try:
    inp = int(inp)
except:
    print('Этот элемент встречается в предложении', s_str, s_str.count(inp), 'раз\n')
else:
    print('Этот элемент встречается в списке', s, s.count(inp), 'раз\n')
    
#8
konv = tuple(s)
print('Сконвертировали список в словарь\n')

#9
print(s)
print('Отсортировали коллекцию')
print(sorted(s))