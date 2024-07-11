#Aplicar as políticas do banco para obter a variavel target

import numpy as np

# 1 Limite de crédito 

dataset_credit_risk["Nome_coluna ou coluna existente"] = np.where((dataset_credit_risk["coluna"] >= 8000) & (dataset_credit_risk["coluna"] <= 12000), 1, 0)
dataset_credit_risk
