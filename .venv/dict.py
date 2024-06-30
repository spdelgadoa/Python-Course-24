numbers = {1:'uno', 2:'dos', 3:'tres'}
print(numbers[2])
information = {'nombre' : 'Sandra',
               'Apellido': 'Delgado',
               'Altura': 1.57,
               'Edad': 33}
print(information)
del information['Edad']
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = {'Sandra':
               {'Apellido': 'Delgado',
               'Altura': 1.57,
               'Edad': 33},
                'Tomas': {'Apellido': 'Lopez',
               'Altura': 1.75,
               'Edad': 32}}
print(contacts)
print(contacts['Sandra'])