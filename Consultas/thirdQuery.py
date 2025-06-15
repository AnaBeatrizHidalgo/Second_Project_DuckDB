import duckdb

# Query com as informações de emissão de CO2 por pais

query = '''
SELECT Country,
       Year,
       Sector,
       CO2_Emission_Sector,
       Power_Source,
       CO2_Emission_Power,
       CO2_Emission_Total
FROM info_pais,
ORDER BY CO2_Emission_Total DESC, Year DESC;    
'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/queryThird.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
