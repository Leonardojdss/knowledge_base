#Converter campos strings para numéricos
#Necessário instalar a lib sklearn

for label in ["COLUNA1", "COLUNA2", "COLUNA3", "COLUNA4","COLUNA5","COLUNA6"]:
    NOME_DO_DATA_SET[label] = LabelEncoder().fit_transform(NOME_DO_DATA_SET[label])
#confirmar se realmente foi alterado
NOME_DO_DATA_SET.info()
