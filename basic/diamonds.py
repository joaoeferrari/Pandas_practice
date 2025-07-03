import pandas as pd
import seaborn as sb

# 1 - Carregue o dataset diamonds e exiba as 5 primeiras linhas
df = sb.load_dataset('diamonds')
df.describe()
df.head()

# 2 - Qual o número total de linhas e colunas?
df.shape

# 3 - Quantos valores únicos existem na coluna cut?
# df['cut'].unique() # quais
df['cut'].nunique() # quantos

# 4 - Qual o tipo de dado de cada coluna?
df.info()

# 5 - Qual o preço médio de um diamante?
df['price'].mean()

# 6 - Qual o menor e o maior valor de quilate (carat)?
df['carat'].max()
df['carat'].min()

# 7 - Filtre os diamantes com mais de 1.5 quilates e preço acima de $10.000.
df.loc[ (df['carat'] > 1.5) & (df['price'] > 10000) ]

# 8 - Calcule o preço médio por categoria de corte (cut)
df.groupby('cut')['price'].mean()

# 9 - Agrupe por cut e color e calcule a média de preço
q9 = df.groupby(['cut', 'color'])['price'].mean().reset_index()

# 10 - Qual combinação de cut e color tem o maior preço médio?
q9.loc[q9['price'].idxmax()] # premium e 3

# 11 - Crie uma nova coluna chamada volum que seja x * y * z.
df['volum'] = df['x'] * df['y'] * df['z']

# 12 - Qual a média do volume para diamantes com preço maior que $5.000?
maior5 = df.loc[df['price']>5000]
maior5['volum'].mean()

# 13 - Crie uma coluna chamada price_per_carat com o preço dividido pelo peso (price / carat)
df['price_per_carat'] = df['price'] / df['carat']

# 14 -Existe correlação entre carat e price? Use o método .corr() para investigar
df[['carat', 'price']].corr()