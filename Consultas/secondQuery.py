import pandas as pd
import duckdb
from sqlalchemy import text

# Query com as informações de energy

query = text('''
Select Country,
       Year,
       Power_Source,
       Power_is_renewable,
       Power_Generation,
       CO2_Emission_Power
FROM info_pais
ORDER BY Power_Generation DESC, CO2_Emission_Power DESC;
''')

with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/SecondQuery.csv")

    print(df.to_string(index=False))
