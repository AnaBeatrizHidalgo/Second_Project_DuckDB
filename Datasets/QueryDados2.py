"""
Este codigo é apenas ilustrativo.
Serve de referencia para entender como foram resgatados os dados do projeto passado: https://github.com/AnaBeatrizHidalgo/First-Database-
Então ao tentar executar neste projeto, o codigo dara erro.
"""

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
        I."Year",
		DP."Population",
        D."IDH",
        D."Electricity",
		D."Sanitation",
		D."Health",
		D."Standard_Living",
        I."GDP",
        I."Investment_Energy",
        I."Health_Expenditure",
        E."CO2_Emision"
FROM    "Country"  C
JOIN "Investment"     I  ON I."Country_ID" =  C."ID_Country"
JOIN "Development"    D  ON D."Country_ID" =  C."ID_Country" AND I."Year" = D."Ano"
JOIN "Demography"     DP ON DP."Country_ID"= C."ID_Country" AND I."Year" = DP."Year"
JOIN "Environmental Indicator" E ON E."Country_ID" = C."ID_Country"  AND I."Year" = E."Year"
ORDER BY C."Name", I."Year" DESC
''')

with engine.begin() as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./DadosSetorEnergy.csv")
