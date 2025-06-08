import pandas as pd
import duckdb
from sqlalchemy import text

# Query para analisar quanto a produção de energia reflete na sua utilização

query = text('''

''')


with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/SixthQuery.csv")

    print(df.to_string(index=False))
