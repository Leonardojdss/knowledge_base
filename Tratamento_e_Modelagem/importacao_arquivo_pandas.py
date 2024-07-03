# Importação do arquivo

import pandas as pd

file_path = "credit_risk_dataset.csv"
dataset_credit_risk = pd.read_csv(file_path, sep=",")

""" O pandas realiza leitura de diversos arquivos, como excel, json, parquet etc, necessario pudar na linha 6 o tipo de arquivo a ser lido"""
