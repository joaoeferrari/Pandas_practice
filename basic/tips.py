import pandas as pd
import seaborn as sb

# 1 - Carregue o dataset tips do Seaborn e mostre as 5 primeiras linhas. 
df = sb.load_dataset('tips')
df.head()

# 2 - Qual o total de linhas e colunas do dataset?
df.shape

# 3 - Quais são os tipos de dados de cada coluna?
df.info()

# 4 - Mostre as estatísticas descritivas (média, mediana, desvio padrão, etc.) para as colunas numéricas
df.describe()

# 5 - Quantos clientes homens e quantos mulheres existem no dataset?
df['sex'].value_counts()

# 6 - Qual a média da gorjeta (tip) para fumantes e não fumantes?
df.groupby('smoker')['tip'].mean()

# 7 - Filtre o dataset para mostrar apenas as refeições feitas no jantar (Dinner). Quantas linhas aparecem?
df.loc[df['time'] == 'Dinner']

# 8 - Qual foi a maior gorjeta em valor absoluto?
df['tip'].max()

# 9 - Mostre o total da conta (total_bill) e a gorjeta (tip) para as mesas com mais de 4 pessoas
q9 = df.loc[df['size'] >= 4]
q9[['total_bill', 'tip', 'size']].head()

# 10 - Agrupe os dados por dia da semana (day) e calcule a média da gorjeta e do total da conta para cada dia
q10 = df.groupby('day')[['tip', 'total_bill']].mean().reset_index()

# 11 - Quais os dias que tiveram a maior e menor média de gorjeta?
q11_maior = q10.loc[q10['tip'].idxmax()]
q11_maior

q11_menor = q10.loc[q10['tip'].idxmin()]
q11_menor

# 12 - Agrupe os dados por sex e smoker e calcule o total e a média das gorjetas
df.groupby(['sex', 'smoker'])['tip'].mean()

# 13 - Ordene o dataset pelo valor da conta (total_bill) em ordem decrescente e mostre as 10 primeiras linhas.
df.sort_values(by='total_bill', ascending=False).head(10)

# 14 - Conte quantas refeições foram feitas em cada período do dia (Lunch e Dinner)
df['time'].value_counts()

# 15 - Mostre as 3 maiores contas (total_bill) feitas por mulheres fumantes.
q15 = df.loc[ (df['sex'] == 'Female') & (df['smoker'] == 'Yes')]

q15.sort_values(by='total_bill', ascending=False).head(3)

# 16 - Crie uma tabela pivot que mostre a média da gorjeta (tip) para cada combinação de dia (day) e período (time)

df.pivot_table(
    values='tip',
    index='day',
    columns='time',
    aggfunc='mean'
)

# 17 - Renomeie a coluna size para party_size
df.rename({'size':'party_size'}, axis=1,inplace=True)




