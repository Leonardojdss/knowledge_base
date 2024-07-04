# Tranformando a variavel target, sera criado a coluna target

# Good = 1 = credito aprovado por ser bom pagador
# Bad = 0 = credito negagado por ser um mal pagador

data_set_original["Target"] = np.where((data_set_original["Risk"] == "good"), 1, 0)
data_set_transformado = data_set_original
data_set_transformado
