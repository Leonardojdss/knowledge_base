data_set_original = [
    {"Risk": "good"},
    {"Risk": "bad"},
    {"Risk": "good"},
    # mais entradas...
]

# Tranformando a variável target
for row in data_set_original:
    if row["Risk"] == "good":
        row["Target"] = 1
    else:
        row["Target"] = 0

data_set_transformado = data_set_original

# Exibir o dataset transformado
print(data_set_transformado)
