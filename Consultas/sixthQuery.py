import pandas as pd
import duckdb
from sqlalchemy import text

# Query para analisar quanto a produção de energia reflete na sua utilização

query = text('''
SELECT
    Country,
    Year,
    SUM(CASE WHEN Power_is_renewable = TRUE THEN Power_Generation ELSE 0) AS Power_Renewable,
    Sum(CASE WHEN Power_is_renewable = FALSE THEN Power_Generation ELSE 0) AS POwer_Not_Renewable,
    Power_Consumed,
    Renewble_Energy,
    Power_Import,
    Eletricity
FROM info_pais
GROUP BY Country, Year, Power_Import, Eletricity, Power_Consumed, Renewble_Energy
ORDER BY Year DESC, Eletricity DESC, Power_Renewable DESC, Power_Consumed DESC
''')


with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/SixthQuery.csv")

    print(df.to_string(index=False))
