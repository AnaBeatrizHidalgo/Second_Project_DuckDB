import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)

# Query com o intuito de analisar a relação entre Country e Power Generation, conseguindo observar qual energia mais emite CO2

query = text('''
SELECT  C."Name"            AS "country",
        P."Year",
		P."GWH" AS "Power_Consumed",
        P."Renewable_Energy" AS "renewable share pct",
        P."PowerImport"      AS "import_gwh",
		S."Name" AS "Sector",
		SC."CO2_Emission" AS "CO2_Emission_Sector",
		PS."Name" AS "Power_Source",
		PS."Renewable" AS "Power_is_renewable",
        CP."Power_Generation" AS "Power_Generation", 
        CP."CO2_Emission" AS "CO2_Emission_Power"
FROM    "Country"  C
JOIN "Power Consumed" P ON P."Country_ID" = C."ID_Country"
JOIN "Power Source_Country" CP ON  CP."Country_ID_Country" = C."ID_Country"  AND P."Year" = CP."Year"
JOIN "Sector_Country" SC ON SC."Country_ID_Country" = C."ID_Country" AND P."Year" = SC."Year"
JOIN "Sector" S ON SC."Sector_ID_Sector" = S."ID_Sector"
JOIN "Power Source" PS ON PS."ID_Power" = CP."Power Source_ID_Power"
ORDER BY C."Name", P."Year" DESC
''')

with engine.begin() as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./DadosDesenvolvimento.csv")
