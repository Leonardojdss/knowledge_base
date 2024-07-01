# Verifica registros duplicados

validacao_de_duplicados = data_set_original.duplicated().sum()

if validacao_de_duplicados == 0:
    print("ótimo, Nao existem registros duplicados")
else:
    print("Existem registros duplicados")
