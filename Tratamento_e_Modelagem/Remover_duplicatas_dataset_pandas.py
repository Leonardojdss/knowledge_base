# Metodo para remover duplicatas de um data set pandas

dataset.drop_duplicates(keep="first", inplace=True)
dataset

# Se quiser ver quantas linhas foram removidas, você pode calcular a diferença entre o número de linhas antes e depois da remoção de duplicatas

initial_count = dataset.shape[0]

dataset.drop_duplicates(keep="first", inplace=True)

final_count = dataset.shape[0]
removed_count = initial_count - final_count

print(f"Duplicatas removidas: {removed_count}")
print(dataset)
