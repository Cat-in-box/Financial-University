d = {('0', '0', '0', '0'): 0, ('0', '0', '0', '1'): 1, ('0', '0', '1', '0'): 2, ('0', '0', '1', '1'): 3, 
     ('0', '1', '0', '0'): 4, ('0', '1', '0', '1'): 5, ('0', '1', '1', '6'): 0, ('0', '1', '1', '1'): 7, 
     ('1', '0', '0', '0'): 8, ('1', '0', '0', '1'): 9, ('1', '0', '1', '10'): 2, ('1', '0', '1', '1'): 11, 
     ('1', '1', '0', '0'): 12, ('1', '1', '0', '1'): 13, ('1', '1', '1', '6'): 14, ('1', '1', '1', '1'): 15}
a = tuple(input('Введите тетраду '))
print(d.get(a))