saludo_1 ="Hola"
saludo_2 = "Hi"
nombre ='Carli'
fullname= '''sandra
delgado

espacios'''
caracter = 'c'
print(saludo_1 * 5)
print(fullname)
#print(type(fullname))
print(fullname[0])
print(fullname[-2])
print(saludo_1 + ' ' +  nombre)
print(len(fullname))
print(len(saludo_1))
print(nombre.lower())
print(nombre.upper())

#Clase 6
print('\n Clase 6 \n')

name = input('Ingrese su nombre: ')
print(name)
print(type(name))
age = int(input('Ingrese su edad '))
print(age)
print(type(age))


#Clase 7
print('\n Clase 7 \n')
to_do = ['Go to Hotel',
         'Go to lunch',
         'Visit museum',
         'Go back to Hotel']
print(to_do)
numbers = [1,2,3,4,'cinco']
print(type(numbers))
mix = ['uno', 2,3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print('1er Elemento: ', mix[0])
print('2do Elemento: ', mix[1])
print('Ultimo Elemento: ', mix[-1])
string = 'hola mundo'
print('1er Elemento: ', string[0])
print('2do Elemento: ', string[1])
print('Ultimo Elemento: ', string[-1])
print(mix[0:2])
print(mix[0:])
print(mix)
mix.append(False)
print(mix)
mix.insert(2,[3,4])
mix.append([3,6])
print(mix)
print(mix.index([3,4]))
numbers = [1,2,100,90.45,3,4,5]
print(numbers)
print('Mayor:', max(numbers))
print('Menor:', min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]


#Clase 8


print('\n Clase 8 \n')

a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c= a[:]
print(id(a))
print(id(b))
a.append(6)
print(a)
print(b)
print(c)
a.append(6)


