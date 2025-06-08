import pandas as pd
import duckdb
from sqlalchemy import text

# Query para analisar qual Setor possui a maior emissão de CO2 no ano de 2023
query = text('''
WITH SectorEmissions AS (
    SELECT 
        Country,
        Sector,
        Year,
        SUM("CO2_Emission_Sector") AS Total_CO2_Emission
    FROM info_pais
    WHERE Year = 2023
    GROUP BY Sector, Country, Year
),
RankedCountries AS (
    SELECT 
        Sector,
        Country,
        Total_CO2_Emission,
        RANK() OVER (PARTITION BY Sector ORDER BY Total_CO2_Emission DESC) AS CountryRank
    FROM SectorEmissions
),
SectorTotals AS (
    SELECT 
        Sector,
        SUM(Total_CO2_Emission) AS Sector_Total_Emission
    FROM SectorEmissions
    GROUP BY Sector
)
SELECT 
    t.Sector,
    t.Sector_Total_Emission,
    r.Country AS Top_Contributor_Country,
    r.Total_CO2_Emission AS Top_Country_Contribution
FROM 
    SectorTotals t
JOIN 
    RankedCountries r ON t.Sector = r.Sector
WHERE 
    r.CountryRank = 1
ORDER BY 
    t.Sector_Total_Emission DESC;
''')

with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/FirstQuery.csv")

    print(df.to_string(index=False))
