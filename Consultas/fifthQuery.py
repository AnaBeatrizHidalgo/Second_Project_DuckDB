import duckdb

# Saber de quanto que o pais investe reflete no seu desenvolvimento

query = '''
SELECT 
    Country,
    Year,
    IDH,
    GDP,
    Electricity,
    Eletricity_Investimente,
    Health,
    Health_Investimente,
    SUM(Power_Generation) AS total_power,
    Renewable_share_pct,
    Power_Import,
    CO2_Emission_Total,
    SUM(CO2_Emission_Power) AS Emission_Energy,
    SUM(CO2_Emission_Sector) AS Emission_Sector
FROM info_pais
GROUP BY Country, Year, IDH, GDP, Electricity, Eletricity_Investimente,
         Health, Health_Investimente, Renewable_share_pct, Power_Import, CO2_Emission_Total
ORDER BY YEAR DESC, IDH DESC, GDP DESC, CO2_Emission_Total DESC
LIMIT 50;
'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/queryFifth.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
