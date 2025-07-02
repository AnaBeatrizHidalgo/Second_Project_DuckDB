import duckdb

# Query reflete a relação linear geral entre % de renovavel e emissões de CO2 em todas essas observações combinadas
# Valor negativo quer dizer que quanto mais renovavel menos CO2

query = '''
SELECT
  corr(Renewable_share_pct, CO2_Emission_Power) AS corr_renew_co2
FROM info_pais
WHERE Renewable_share_pct IS NOT NULL
  AND CO2_Emission_Power IS NOT NULL;
'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/queryThird.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
