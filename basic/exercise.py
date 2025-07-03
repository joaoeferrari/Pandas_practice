import pandas as pd
import seaborn as sb

# 1 - Carregue o dataset exercise e exiba as 5 primeiras linhas
df = sb.load_dataset('exercise')
df.head()

# 2 - Quantos participantes únicos existem (id)?
df['id'].nunique()

# 3 - Quais são os tipos de exercício presentes na coluna kind?
df['kind'].unique()

# 4 - Quantos registros existem para cada tipo de dieta?
df['kind'].value_counts()

# 5 - Qual a frequência cardíaca média geral (pulse)?
df['pulse'].mean()

# 6 - Qual foi a frequência cardíaca média para o exercício running?
q6 = df.loc[df['kind'] == 'running'].reset_index(drop=True)
q6['pulse'].mean()

# 7 - Quais participantes (id) tiveram pulse acima de 150 em qualquer exercício?

q7 = df.loc[df['pulse'] > 150].reset_index(drop=True)
q7['id']

# 8 - Filtre os dados para mostrar apenas exercícios de 30 minutos e dieta no fat
df[(df['time'] == '30 min') & (df['diet'] == 'no fat')]

# 9 - Calcule a média do pulse por tipo de exercício (kind)
df.groupby('kind')['pulse'].mean()

# 10 - Calcule a média do pulse por diet e time
df.groupby(['diet', 'time'])['pulse'].mean().reset_index()

# 11 - Qual combinação de dieta + tipo de exercício teve o maior pulse médio?
q11 = df.groupby(['diet', 'kind'])['pulse'].mean().reset_index()
q11.loc[q11['pulse'].idxmax()]

# 12 - Crie uma nova coluna chamada pulse_zone, onde: pulse < 100 → 'low', pulse entre 100–140 → 'moderate', pulse > 140 → 'high'
df['pulse_zone'] = pd.cut(df['pulse'], bins=[0, 100, 140, df['pulse'].max()], labels=['low', 'moderate', 'high'])
df.head()

# 13 - Quantas observações há em cada pulse_zone?
df['pulse_zone'].value_counts()

# 14 - Crie uma pivot_table com kind nas linhas, time nas colunas, e média de pulse como valores
df.pivot_table(
    values='pulse',
    index='kind',
    columns='time',
    aggfunc='mean'
)

# 15 - Qual dieta teve maior média de pulse após 15 minutos de running?
q15 = df.loc[(df['kind'] == 'running') & (df['time'] == '15 min')]
q15.groupby('diet')['pulse'].mean().reset_index()

# 16 Existe diferença significativa na média de pulse entre walking e rest? 
df['kind'].unique()


media_pulse_rest = df.loc[df['kind'] == 'rest']
media_pulse_rest['pulse'].mean()

media_pulse_walking = df.loc[df['kind'] == 'walking']
media_pulse_walking['pulse'].mean()


 