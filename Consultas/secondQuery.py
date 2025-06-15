import duckdb

# Query com as informações de energy

query ='''
Select Country,
       Year,
       Power_Source,
       Power_is_renewable,
       Power_Generation,
       CO2_Emission_Power
FROM info_pais
ORDER BY Power_Generation DESC, CO2_Emission_Power DESC, Year DESC;
'''


with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/querySecond.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
