import duckdb

# Query com as informações de energy

query ='''
SELECT
  Country,
  ROUND(AVG(Renewable_share_pct), 2) AS avg_renewable_pct
FROM info_pais
WHERE Year BETWEEN EXTRACT(YEAR FROM CURRENT_DATE) - 9 AND EXTRACT(YEAR FROM CURRENT_DATE)
  AND Renewable_share_pct IS NOT NULL
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY avg_renewable_pct DESC
LIMIT 10;
'''


with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/querySecond.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
