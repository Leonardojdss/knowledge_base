#funcoes

def exibir_menu():
    print("1 - somar")
    print("2 - subtracao")
    print("3 - divisao")
    print("0 - sair")

def somar(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    return num1 / num2

continuar = 1 or 2 or 3
while continuar != 0:
    exibir_menu()
    opcao = int(input('opcao:'))
    if opcao == 1:
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        saida = somar(n1, n2)
        print("a soma e igual", saida)
    elif opcao == 2:
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        saida = subtracao(n1, n2)
        print("a subtracao e igual", saida)
    elif opcao == 3:
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        saida = divisao(n1, n2)
        print("a divisao e igual", saida)
    elif opcao == 0:
        continuar = 0
        print('programa encerrado')
