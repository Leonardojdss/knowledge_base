#listas

#criando uma lista
valores = [1, 2, 3, 4, 5, -4, 0, -10, 304]

#acessando uma lista
print(valores)

#acessando uma posicao da lista
print(valores[1])

#trocando um valor da lista
valores[1] = 9
print(valores)

#encontrando o maior valor da lista
print('o maior valor da lista e:', max(valores))

#encontrando o menor valor da lista 
print('encontrando o menor valor da lista', min(valores))

#valor medio da lista
print("encontrando o valor medio da lista", round(sum(valores)/len(valores),2))

#passa por todos os valores da lista
for valor in valores:
    print(valor)