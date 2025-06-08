import pandas as pd
import duckdb
from sqlalchemy import text

# Query com as informações de emissão de CO2 por pais

query = text('''
SELECT Country,
       Year,
       Sector,
       CO2_Emission_Sector,
       Power_Source,
       CO2_Emission_Power,
       CO2_Emission_Total
FROM info_pais,
GROUP BY CO2_Emission_Total;    
''')

with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/ThirdQuery.csv")

    print(df.to_string(index=False))
