#Exemplo para resolver problemas onde existe valores nulo, para resolver esses outliers pode ser usado a média

media_close = df["Nome_coluna"].mean()

for outlier in outliers:
    df["Nome_coluna"].replace(outlier, media_close, inplace=True)

df
