# Realizando consultas - usando o método select

NOME_DO_DATA_FRAME\
    .select("*")\
    .show(5, truncate=False)

# * = selecionando todas as colunas
# 5 = Retornas as primeiras 5 colunas
# truncate = false, não truncar os dados das colunas

# selecionando colunas desejadas

NOME_DO_DATA_FRAME\
    .select("COLUNA1", "COLUNA2", "COLUNA3")\
    .show(5, truncate=False)
