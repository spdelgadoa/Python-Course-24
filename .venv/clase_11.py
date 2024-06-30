x = 5
if x > 5:
    print('X es mayor que 5')
elif x == 5:
    print('X es igual que 5')
else:
    print('X es menor que 5')
print('Afuera')



#dos variables

x = 15
y = 20

if x>10 and y>25:
    print('X es > que 10 y Y es < que 15')

if x>10 or y>25:
    print('X es > que 10 O Y es mayor que 25')

if not x>10:
    print('X no es mayor que 10')

#otro caso

is_member = False
age = 15

if is_member:
    if age >= 15:
        print('Tienes acceso porque eres miembro')
    else:
        print('No tienes acceso ya que eres miembro pero menor a 15 años')
else: 
    print('No eres miembro y No tienes acceso')
