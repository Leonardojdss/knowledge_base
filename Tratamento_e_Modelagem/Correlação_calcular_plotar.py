# Calculando as correlacoes

correlacoes = x.corr()

# plotando a correlacao

plt.figure(figsize=(10,10))
sns.heatmap(data=correlacoes, annot=True)
plt.show()
