# contagem de nulos por colunas

NOME_DATA_FRAME.select([f.count(f.when(f.isnull(c), 1)).alias(c) for c in NOME_DATA_FRAME.columns]).show()
