import random
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
user = int(input('Esolha uma opcao:\n[0]Pedra\n[1]Papel\n[2]Tesoura\nDigite sua escolha:'))
print('')
print('JON')
sleep(1)
print('KEN')
sleep(1)
print('POOW!!!')
print('')
print('-=-' * 20)
print('O computador escolheu {}'.format(lista[computador]))
print('o Jogador escolheu {}'.format(lista[user]))
print('-=-' * 20)
if computador == 0:
    if user == 0:
        print('Empatou!')
    elif user == 1:
        print('Voce ganhou!')
    elif user == 2:
        print('Voce perdeu!')
    else:
        print('Comando invalido! Tente novamente!')
elif computador == 1:
    if user == 1:
        print('Empatou')
    elif user == 0:
        print('Voce perdeu!!')
    elif user == 2:
        print('Voce Ganhou!')
    else:
        print('Comando invalido! Tente novamente!')

elif computador == 2:
    if user == 2:
        print('Empatou!')
    elif user == 0:
        print('Voce ganhou!')
    elif user == 1:
        print('Voce perdeu!!!')
    else:
        print('Comando invalido! Tente novamente!')