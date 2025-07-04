import pandas as pd
import seaborn as sb

df = sb.load_dataset("flights")
df.head()

df.shape

# 1 - Registros do ano de 1950
df.loc[df['year'] == 1950 ]

# 2 - Registros dos meses de junho a agosto

# df.loc[df['month'] == 'Jun'].shape[0]
# df.loc[df['month'] == 'Jul'].shape[0]
# df.loc[df['month'] == 'Aug'].shape[0]

df[df['month'].isin(['Jun', 'Jul', 'Aug'])]

# 3 - Meses com mais de 400 passageiros
df.loc[df['passengers'] > 400]

# 4 - Meses com passageiros entre 250 e 350 (inclusive)

# res 1
df.loc[(df['passengers'] >= 250) & (df['passengers'] <= 350)]
# res 2
df[df['passengers'].between(250, 350)]


# 5 - Anos em que dezembro teve mais de 400 passageiros

# res 1
df.loc[ (df['month'] == 'Dec') & (df['passengers'] > 400) ]
# res 2 
df[(df['month'] == 'Dec') & (df['passengers'] > 400)]['year'].unique()

# 6 - Registros dos meses Jan, Feb, Mar com isin()
df[ df['month'].isin(['Jan', 'Feb', 'Mar'])]

#- 7 - Registros com passageiros > 300 e mês igual a 'July' (query)
df.query("passengers > 300 & month == 'Jul' ")

# 8 - Registros entre os anos de 1952 e 1956 (inclusive)
df[ df['year'].between(1950,1956) ]

# 9 - Passageiros < 150 e anos até 1951
df.loc[ (df['passengers'] < 150) & ( df['year'] <= 1951 )  ]

# 10 - Passageiros > 450 OU mês = 'Dec'
df.loc[ ( df['passengers'] > 450 ) | ( df['month'] == 'Dec' ) ]

# 11 - Para cada ano, mês com maior número de passageiros
q11=df.groupby('year')['passengers'].idxmax()
df.loc[q11].sort_values('year')

# 12 - Ano com maior número total de passageiros
anos = df.groupby('year')['passengers'].sum().reset_index().sort_values('year')
ano_mac = anos.loc[anos['passengers'].idxmax()] 

# 13 - Exiba apenas year e passengers dos registros com mais de 420 passageiros
df.loc[df['passengers'] > 420, ['year', 'passengers']]

# 14 - Mostrar registros onde passageiros > média geral
media_geral = df['passengers'].mean()
df.loc[df['passengers'] > media_geral, ['year', 'month', 'passengers']]

# 15 - Qual a média de passageiros apenas nos meses de 'Jun' e 'Jul'?

# media_jun = df.loc[df['month'] == 'Jun', 'passengers'].mean()
# media_jul = df.loc[df['month'] == 'Jul', 'passengers'].mean()
# media_JunJul = (media_jun + media_jul) / 2

df[df['month'].isin(['Jun', 'Jul'])]['passengers'].mean()

# 16 - Criar coluna 'passenger_level': baixo < 200, médio 200–400, alto > 400

df['passenger_level'] = pd.cut(df['passengers'], 
                                bins=[0,200,400,df['passengers'].max()],
                                labels=['baixo','medio','alto'])

# 17 - Mostre quantos meses caem em cada categoria da coluna passenger_level
df.groupby('passenger_level')['month'].count().reset_index()
df['passenger_level'].value_counts()

# 18 Verificar se há lnhas duplicadas
df.duplicated().sum()