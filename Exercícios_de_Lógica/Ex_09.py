#lista manipulacao

#criando uma lista e apresentando ela
lista = [1, 2, 4, 67]
print(lista)

#adicionando novos membros nesta lista
lista.append(12)
lista.append(3)
print(lista)

#utilizando o metodo sorted para ordenar de forma crescente
lista_ordenada_crescente = sorted (lista)
print(lista_ordenada_crescente)

#utilizando o metodo sorted para ordenar de forma decrescente
lista_ordenada_decrescente = sorted (lista, reverse=True)
print(lista_ordenada_decrescente)

