import random
nome = {}
quantidade = int(input('Digite a quantidade de participantes do sorteio: \n'))

for i in range(1, quantidade+1):
    nome[i] = input('Digite o nome do participante: \n')

print(f'O sorteado foi: {random.choice(list(nome.values()))}')
