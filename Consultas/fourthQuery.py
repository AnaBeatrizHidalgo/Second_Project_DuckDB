import pandas as pd
import duckdb
from sqlalchemy import text

# Query com as informações de emissão de CO2 globalmente,  extraindo o pais, o sector e a energia que mais emitem CO2

query = text('''
WITH SectorEmissions AS (
    SELECT
        Sector,
        Year,
        SUM("CO2_Emission_Sector") AS Sector_Emission
    FROM info_pais
    GROUP BY Year, Sector
),
EnergyEmission AS (
    SELECT 
        Year,
        Power_Source,
        SUM(CO2_Emission_Power)  AS Power_Emission
    FROM info_pais
    GROUP BY Year , Power_Source
),
CountryEmission AS (
    SELECT 
        Country,
        Year,
        CO2_Emission_Total AS Country_Emission
    FROM info_pais
    GROUP BY Year, Country
),
TotalIDH AS (
    SELECT 
        SUM(IDH) AS Total_IDH,
        Year
    FROM info_pais
    GROUP BY Year
),
TotalGDP AS (
    SELECT
        SUM(GDP) AS Total_GDP,
        Year
    FROM info_pais
    GROUP BY Year
),
SELECT 
    ip."Year",
    (SELECT Sector_Emission FROM SectorEmissions AS se WHERE se."Year" = ip."Year") AS co2_total_sector,
    (SELECT Sector FROM SectorEmissions  AS se WHERE se."Year" = y."Year" ORDER BY SectorEmissions DESC LIMIT 1) AS sector_maior_emissao,
    (SELECT Power_Emission FROM EnergyEmission AS ce WHERE ce."Year" = y."Year") AS co2_total_energia,
    (SELECT energy_name FROM EnergyEmission AS ce WHERE ce."Year" = y."Year" ORDER BY EnergyEmission DESC LIMIT 1) AS energia_maior_emissao,
    (SELECT SUM(Country_Emission) FROM CountryEmission  AS cc WHERE cc."Year" = y."Year") AS co2_total_country,
    (SELECT Country FROM CountryEmission  AS cc WHERE cc."Year" = y."Year" ORDER BY CountryEmission DESC LIMIT 1) AS country_maior_emissao,
    (SELECT Total_IDH FROM TotalIDH AS i WHERE i."Year" = y."Year") AS total_IDH,
    (SELECT Total_GDP FROM TotalGDP AS g  WHERE g."Year" = y."Year") AS total_GDP
FROM info_pais AS ip
ORDER BY co2_total_country DESC, co2_total_energia DESC, co2_total_sector DESC
LIMIT 10; 
''')

with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/FourthQuery.csv")

    print(df.to_string(index=False))
