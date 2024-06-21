#Estrutura de repeticao while

segredo = 42

palpite = int(input("informe um valor:"))

while segredo != palpite:
    palpite = int(input("informe um valor:"))
    if palpite > segredo:
        print('tente novamente com um numero menor')
    elif palpite < segredo:
        print('tente novamente com um numero maior')

print('parabens seu palpite esta correto, sendo', palpite)
    