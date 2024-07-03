#Criando um arquivo CSV, exemplo utilizando o dataset de ações

name = 'NVDA'
file = os.path.join(folder, f'{name}.csv')
data = yf.download(name, start='2004-01-01', end='2024-06-19')
data.to_csv(file)
df = pd.read_csv(file)
df
