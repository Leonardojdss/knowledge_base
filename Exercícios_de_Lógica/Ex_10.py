#Dicionario

#Criando um dicionario
pontos = {}

pontos["Vitorias"] = 3
pontos["derrotas"] = 2
pontos["empates"] = 0

#exibe os dados dentro do dicionario
print(pontos)

#adicionando mais valor em uma das chaves
pontos['Vitorias'] += 1

#passando por todos os valores do dicionarios
for chave, valor in pontos.items():
    print('chave:', chave, 'valor:', valor)

print(pontos.items())