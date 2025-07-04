import pandas as pd
import seaborn as sb

df = sb.load_dataset('iris')
df.head()

# 1 - Mostrar registros da espécie 'setosa'
df[df['species'] == 'setosa']

# 2 -  Mostrar registros com comprimento da sépala maior que 6.0
df[df['sepal_length'] > 6]

# 3 - Mostrar registros com largura da sépala entre 3.0 e 3.5 (inclusive)
df[df['sepal_width'].between(3, 3.5)]

# 4 - Mostrar registros da espécie 'virginica' com comprimento da pétala > 5
df[( df['species'] == 'virginica' ) & ( df['sepal_length'] > 5 )]

# 5 -  Mostrar registros com comprimento da pétala menor que 2 OU largura da pétala maior que 2
df[(df['sepal_length'] > 2) | (df['sepal_width'] > 2)]

# 6 -  Mostrar as espécies distintas do dataset
df['species'].unique()

# 7 -  Quantos registros existem para cada espécie?
df['species'].value_counts()

# 8 -  Calcular a média de comprimento da sépala por espécie
df.groupby('species')['sepal_length'].mean().reset_index()

# 9 - Criar coluna "petal_category": curta (<3), média (3-5), longa (>5)
df['petal_category'] = pd.cut(
                            df['petal_length'],
                            bins=[0,3,5, df['petal_length'].max()],
                            labels=['curto', 'medio', 'longo']
                        )

# 10 - Quantos registros em cada categoria de "petal_category"?
df['petal_category'].value_counts()

# 11 - Qual espécie tem maior largura média de pétala?

# res 1
df.groupby('species')['petal_width'].mean().reset_index().max()[0]

# res 2
df.groupby('species')['petal_width'].mean().reset_index().sort_values(by='petal_width', ascending=False).head(1)

# 12 - Mostrar registros com todos os valores maiores que a média da respectiva coluna
medias = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()

df[
    (df['sepal_length'] > medias['sepal_length']) &
    (df['sepal_width'] > medias['sepal_width']) &
    (df['petal_length'] > medias['petal_length']) &
    (df['petal_width'] > medias['petal_width']) 
]

# 13 - Mostrar apenas colunas numéricas para registros da espécie 'versicolor'

df[df['species'] == 'versicolor'].select_dtypes(include='number')

# 14 - Criar coluna "area_petal" = comprimento * largura da pétala

df['area_petal'] = df['petal_length'] * df['petal_width']

df[['petal_length', 'petal_width', 'area_petal']]

# 15 - Quais registros têm "area_petal" acima da média?

# res 1
media_area = df['area_petal'].mean()

df[df['area_petal'] > media_area]

# res 2 
df[df['area_petal'] > df['area_petal'].mean()]

# 16 - Mostrar apenas os 5 registros com maior "area_petal"

df.sort_values('area_petal', ascending=False).head()

# 17 - Mostrar registros com petal_width > 1.5 ordenados pela espécie

df[ df['petal_width'] > 1.5 ].sort_values('species')


# 18 - Verificar se há valores duplicados
df.duplicated().sum()

