#import sys
# sets : son colecciones desordenadas de objetos unicos

# canasta = {'manzana','platano','pera','manzana'}
# print(canasta)

# numero = {1,3,4,5,3,5}
# numero1 = (1,3,4,5,3,5)

# print(numero)
# print(numero1)

# a =  set('abracadabra') #mutables, se pueden anadir nuevos elementos
# print(a)

# b = frozenset('perro')
# print(b)


#recursividad es una funcion que se llama a si misma una y otra vez hasta que cumpla
#una condicion 

from multiprocessing.sharedctypes import Value


array = [10,2,3,2,3,5]
min = array[0]

# for i in range(0,len(array)):
#     print(min)
#     print(array[i])
#     print('*******')
#     if min > array[i]:
#         min = array[i]
     
# print(min)



# dic =  {1 : 'c', 2 : 'b', 3 : 'c' , 4 : 'd'}

# for i in range(1, 5):
    
#     if dic[i] == 'c':
#         print(i, "es la que seleccionso")
    
#     if dic[i].get('b') == 2:
#         a = dic[i]

# print(a)

dic = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
valor = dic.pop('b')
valor = dic.pop('a')
 
print(dic)