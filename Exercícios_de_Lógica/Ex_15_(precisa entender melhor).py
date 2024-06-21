#manipulação de objeto

from random import randint

class jogador():
    def __init__(self, nome, email, vitorias, ):
        self.nome = nome
        self.email = email
        self.vitorias = vitorias
        self.Numero = 0
    def sortear_jogada(self):
        self.Numero = randint(1,20)

class jogo():
    def __init__(self, jogador_1, jogador_2):
        self.player1 = jogador_1
        self.player2 = jogador_2

    def compara_jogadores(self):
        if self.player1.Numero > self.player2.Numero:
            self.player1.vitorias += 1
        elif self.player2.Numero > self.player1.Numero:
            self.player2.vitorias += 1
    
    def jogar(self):
        for i in range(7):
            self.player1.sortear_jogada()
            self.player2.sortear_jogada()

            self.compara_jogadores()

            print("##############################")
            print("jogador 1:", self.player1.Numero, self.player1.vitorias)
            print("jogador 2:", self.player2.Numero, self.player2.vitorias)

jogador_1 = jogador("Leonardo", "emailteste@teste.com", 4)
jogador_2 = jogador("Bianca", "biateste@teste.com", 3)

jogo = jogo(jogador_1, jogador_2)
jogo.jogar()

print("----------------------------------------")
if jogador_1.vitorias > jogador_2.vitorias:
    print('Jogador 1 venceu!')
elif jogador_2.vitorias > jogador_1.vitorias:
    print('Jogador 2 venceu!')
else:
    print("empate")