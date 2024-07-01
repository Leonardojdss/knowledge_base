#Converter campos strings para numéricos

for label in ["Sex", "Housing", "Saving accounts", "Checking account","Purpose","Risk"]:
    data_set_transformado[label] = LabelEncoder().fit_transform(data_set_transformado[label])
#confirmar se realmente foi alterado
data_set_transformado.info()
