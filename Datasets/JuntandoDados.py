import pandas as pd

# Carregar os arquivos CSV
df_energy = pd.read_csv('./DadosSetorEnergy.csv')
df_desenvolvimento = pd.read_csv('./DadosDesenvolvimento.csv')

# Padronizar os nomes das colunas comuns (caso haja diferenças)
df_desenvolvimento.rename(columns={'country': 'Country'}, inplace=True)
df_energy.rename(columns={'Country': 'Country'}, inplace=True)  # Para garantir consistência

# Converter Year para o mesmo tipo em ambos DataFrames
df_desenvolvimento['Year'] = df_desenvolvimento['Year'].astype(int)
df_energy['Year'] = df_energy['Year'].astype(int)

# Realizar o merge (junção) dos DataFrames
# Usamos outer join para manter todos os registros de ambos os arquivos
df_merged = pd.merge(df_desenvolvimento, df_energy, 
                     on=['Country', 'Year'], 
                     how='outer',
                     suffixes=('_dev', '_energy'))

# Salvar o resultado em um novo arquivo CSV
df_merged.to_csv('./DadosCompletos.csv', index=False)

print("Arquivos combinados com sucesso! Resultado salvo em 'DadosCompletos.csv'")
