import pandas as pd
import duckdb
from sqlalchemy import text

# Saber de quanto que o pais investe reflete no seu desenvolvimento

query = text('''
SELECT 
    Country,
    Year,
    IDH,
    GDP,
    Eletricity,
    Eletricity_Investimente,
    Health,
    Health_Investimente,
    SUM(Power_Generation) AS total_power,
    Renewble_Energy AS Pct_Energy_Reneable_Use,
    Power_Import,
    CO2_Emission_Total,
    SUM(CO2_Emission_Power) AS Emission_Energy,
    SUM(CO2_Emission_Sector) AS Emission_Sector
FROM info_pais
GROUP BY Country, Year, IDH, GDP, Eletricity, Eletricity_Investimente,
         Health, Health_Investimente, Renewble_Energy, Power_Import, CO2_Emission_Total
ORDER BY YEAR DESC, IDH DESC, GDP DESC, CO2_Emission_Total DESC
LIMIT 50;
''')

with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/FifithQuery.csv")

    print(df.to_string(index=False))
