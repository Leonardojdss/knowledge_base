# Analisando as colunas que possuem dados faltantes, contagem de nulos ou nan por colunas

NOME_DATA_SET\
    .select([f.count(f.when(f.isnull(c) | f.isnan(c), True)).alias(c) for c in NOME_DATA_SET.columns])\
    .show()
