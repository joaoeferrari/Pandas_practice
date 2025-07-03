import pandas as pd
import seaborn as sb

df = sb.load_dataset("titanic")
df.head()

df.shape

# 1 Mostrar todos os passageiros da 1ª classe
df[df['pclass'] == 1] 

# 2 Mostrar apenas passageiros com idade menor que 18
df[df['age'] < 18 ]

# 3 Mostrar passageiros que embarcaram no porto 'S'
df[ df['embarked'] == 'S' ]

# 3a. Colunas específicas passageiros que embarcaram no porto 'S'
df.loc[ df['embarked'] == 'S', ['pclass', 'age', 'embarked'] ]

# 4 Mostrar passageiros que sobreviveram e eram do sexo feminino
df[ (df['survived'] == 1 ) & (df['sex'] == 'female') ]

# 5 Mostrar passageiros com tarifa entre 100 e 200
df[df['fare'].between(100,200)]

# 6 Mostrar os passageiros do sexo masculino com idade entre 30 e 50 anos
df[ (df['sex'] == 'male') & (df['age'].between(30,50)) ]

# 7 Mostrar os passageiros que estavam sozinhos (sibsp = 0 e parch = 0)
df [ (df['sibsp'] == 0 ) & (df['parch'] == 0) ]

# 8  Mostrar para cada porto de embarque, o número de sobreviventes
df[ df['survived'] == 1 ].groupby('embarked')['survived'].count().reset_index()

# 9 Calcular a média de idade por sexo e classe (pclass)
df.groupby(['sex', 'pclass'])['age'].mean().reset_index()

# 10 Criar coluna 'faixa_idade': 0-18, 19-40, >40

df['faixa_idade'] = pd.cut(
                        df['age'], 
                        bins=[0, 18, 40, df['age'].max()], 
                        labels=['jovem', 'adulto', 'idoso']
                    ) 

# 11 Quantos passageiros em cada faixa de idade?
df['faixa_idade'].value_counts().reset_index()

# 12 Qual faixa de idade teve maior media de sobrevivência?
df.groupby('faixa_idade')['survived'].mean().reset_index()

# 13 Quantos passageiros tinham filhos ou pais a bordo? (parch > 0)
df[df['parch']>0].shape[0]

# 14 Mostrar passageiros que pagaram a tarifa máxima
df[ df['fare'] == df['fare'].max() ]

# 15 Verificar se há linhas duplicadas
df.duplicated().sum()