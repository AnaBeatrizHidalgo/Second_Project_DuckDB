import pandas as pd
import duckdb
from sqlalchemy import text

# Saber de quanto que o pais investe reflete no seu desenvolvimento

query = text('''

''')

with duckdb.connect("project.db") as conn:
    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv("./Consultas/FifithQuery.csv")

    print(df.to_string(index=False))
