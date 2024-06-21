#dicionarios pt 2

from random import randint

def criar_jogador(nome, email, vitorias):
    return {
        "Nome":nome,
        "Email":email,
        "Vistorias":vitorias,
        'Numero': -1
    }

def sortear_jogador():
    return randint(1,20)

def compara_jogadores(player1, player2):
    if player1["Numero"] > player2["Numero"]:
        player1['Vistorias'] += 1
    elif player2["Numero"] > player1["Numero"]:
        player2['Vistorias'] += 1

jogador_1 = criar_jogador("Leonardo", "emailteste@teste.com", 4)
jogador_2 = criar_jogador("Bianca", "biateste@teste.com", 3)

for i in range(7):
    jogador_1['Numero'] = sortear_jogador()
    jogador_2['Numero'] = sortear_jogador()

    compara_jogadores(jogador_1, jogador_2)

    print(jogador_1)
    print(jogador_2)

print("----------------------------------------")
if jogador_1['Vistorias'] > jogador_2['Vistorias']:
    print('Jogador 1 venceu!')
elif jogador_2['Vistorias'] > jogador_1['Vistorias']:
    print('Jogador 2 venceu!')
else:
    print("empate")