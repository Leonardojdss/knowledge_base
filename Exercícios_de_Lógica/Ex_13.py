#Manipulacao de arquivos

#criar arquivo csv
nome_arquivo = "./minha_tabuada.csv"

#iterar no arquivo para criar a tabuada do 1000
arquivo = open(nome_arquivo, 'w')
for numero in range(101):
    saida = ""
    for i in range(1,11):
        saida += f"{numero * i},"
    saida = saida[:-1] + "\n"
    arquivo.write(saida)