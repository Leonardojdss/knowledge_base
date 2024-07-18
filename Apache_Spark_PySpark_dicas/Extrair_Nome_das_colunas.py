# Em uma regressão linear é importante criarmos uma variavel chamada de X que contem o nome de todas colunas 
# que são features, para extrair o nome das colunas pode ser usado o comando a seguir:

SEU_DATA_FRAME.columns

# Retorno será uma lista, exemplo de um dataframe qualquer:

['customerID',
 'unit',
 'usage',
 'bathrooms',
 'bedrooms',
 'floors',
 'parkingSpaces',
 'suites',
 'unitFloor',
 'unitsOnTheFloor',
 'usableAreas',
 'neighborhood',
 'zone',
 'label',
 'condo',
 'iptu',
 'Apartamento',
 'Casa']

# Lembrando que quando você for criado a variavel X voce deve remover o target da lista gerada, no meu exemplo o meu target é price
# então eu removo ele da lista gerada de forma manual.
