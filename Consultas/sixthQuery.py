import duckdb

# Query para analisar quanto a produção de energia reflete na sua utilização

query = '''
SELECT
    Country,
    Year,
    SUM(CASE WHEN Power_is_renewable = TRUE THEN Power_Generation ELSE 0 END) AS Power_Renewable,
    SUM(CASE WHEN Power_is_renewable = FALSE THEN Power_Generation ELSE 0 END) AS Power_Not_Renewable,
    AVG(Power_Consumed) AS Power_Consumed,
    AVG(Renewable_share_pct) AS Renewable_share_pct,
    AVG(Power_Import) AS Power_Import,
    AVG(Electricity) AS Electricity
FROM info_pais
GROUP BY Country, Year
ORDER BY Year DESC, Power_Renewable DESC, Power_Consumed DESC,  Electricity DESC;
'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/querySixth.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
