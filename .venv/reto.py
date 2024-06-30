print('BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA')
print('JUGADOR 1 INGRESA TU NOMBRE: ')
player_1_name = input()
print('JUGADOR 2 INGRESA TU NOMBRE: ')
player_2_name = input()
print(player_1_name, ' ingresa qué eliges: ¿piedra, papel o tijera?: ')
player_1_move = input().lower()
print(player_2_name, ' ingresa qué eliges: ¿piedra, papel o tijera?: ')
player_2_move = input().lower()

valid_moves = ['piedra', 'papel','tijera']

if player_1_move not in valid_moves or player_2_move not in valid_moves:
    print('Uno o ambos jugadores hicieron una elección no válida. Por favor, elijan entre piedra, papel o tijera.')
else:
    if player_1_move == player_2_move:
        print('Empate')
    elif(player_1_move == 'piedra' and player_2_move == 'tijera') or (player_1_move == 'tijera' and player_2_move == 'papel') or    (player_1_move == 'papel' and player_2_move == 'piedra'):
        print('Gana: ', player_1_name)
    else:
        print('Gana: ', player_2_name)

'''if player_1_move == 'piedra':
    if player_2_move =='piedra':
        print('Empate')
    elif player_2_move == 'papel':
        print('Gana: ', player_2_name)
    elif player_2_move == 'tijera':
        print('Gana: ', player_1_name)
elif player_1_move == 'tijera':
    if player_2_move =='piedra':
        print('Gana: ', player_2_name)
    elif player_2_move == 'papel':
        print('Gana: ', player_1_name)
    elif player_2_move == 'tijera':
        print('Empate')
else:
    if player_2_move =='piedra':
        print('Gana: ', player_1_name)
    elif player_2_move == 'papel':
        print('Empate')
    elif player_2_move == 'tijera':
        print('Gana: ', player_2_name)


'''