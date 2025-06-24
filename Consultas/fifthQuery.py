import duckdb
import os

# Garante que a pasta de saída existe
os.makedirs("./Consultas", exist_ok=True)

# Consulta: investimento x desenvolvimento — somente com IDH/GDP válidos
query = '''
SELECT
    Country,
    Year,
    MAX(IDH)                      AS IDH,
    MAX(GDP)                      AS GDP,
    MAX(Electricity)              AS Electricity,
    MAX(Eletricity_Investimente)  AS Eletricity_Investimente,
    MAX(Health)                   AS Health,
    MAX(Health_Investimente)      AS Health_Investimente,
    SUM(Power_Generation)         AS total_power,
    MAX(Renewable_share_pct)      AS Renewable_share_pct,
    MAX(Power_Import)             AS Power_Import,
    MAX(CO2_Emission_Total)       AS CO2_Emission_Total,
    SUM(CO2_Emission_Power)       AS Emission_Energy,
    SUM(CO2_Emission_Sector)      AS Emission_Sector
FROM info_pais
WHERE IDH IS NOT NULL AND GDP IS NOT NULL
GROUP BY Country, Year
ORDER BY Year DESC,
         IDH DESC,
         GDP DESC,
         CO2_Emission_Total DESC
LIMIT 50;
'''

with duckdb.connect("project.db") as con:
    df = con.execute(query).fetchdf()
    df.to_csv("./Consultas/queryFifth.csv", index=False)
    print(df)
