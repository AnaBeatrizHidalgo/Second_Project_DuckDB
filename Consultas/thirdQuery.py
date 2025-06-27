import duckdb

# Query com as informações de emissão de CO2 por pais

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
