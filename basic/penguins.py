import pandas as pd
import seaborn as sb

# 1 - Carregue o dataset e exiba as 5 primeiras linhas
df = sb.load_dataset("penguins")
df.head()

# df.info()

# 2 - Quais colunas possuem valores nulos?
df.isnull().sum()

# 3 - Quais espécies estão presentes no dataset?
df['species'].unique()

# 4 - Quantos pinguins foram registrados em cada ilha?
df['island'].value_counts()

# 5 - Qual a massa corporal média dos pinguins?
df['body_mass_g'].mean()

# 6 - Qual o comprimento médio do bico dos pinguins da espécie Adelie?
df.loc[df['species'] == 'Adelie', 'bill_depth_mm'].mean()

# 7 - Quantos pinguins têm massa corporal maior que 5000g?

# q7 = df.loc[df['body_mass_g'] > 5000]
# len(q7)

df.loc[df['body_mass_g'] > 5000].shape[0]

# 8 - Mostre os pinguins machos (sex == 'Male') com nadadeira (flipper_length_mm) maior que 220mm
df.loc[ (df['sex'] == 'Male') & ( df['flipper_length_mm'] > 200 ) ]

# 9 - Qual a média da massa corporal por espécie?
df.groupby('species')['body_mass_g'].mean().reset_index()

# 10 - Qual a média do comprimento do bico por ilha e por espécie?
df.groupby(['island', 'species'])['bill_length_mm'].mean().reset_index()

# 11 - Qual grupo (espécie + sexo) tem a maior massa corporal média?
df.groupby(['species', 'sex'])['body_mass_g'].mean().reset_index().max()[[0,1]]

# 12 Crie uma nova coluna chamada mass_category, categorizando: < 3500g → 'leve', 3500–4500g → 'médio', > 4500g → 'pesado'

df['mass_category'] = pd.cut(df['body_mass_g'], bins=[0, 3499, 4500, df['body_mass_g'].max()], labels=['leve', 'medio', 'pesado']) # dataframe, intervalos, rotulos

# 13 - Quantos pinguins existem em cada categoria (mass_category)?
df['mass_category'].value_counts()




