import duckdb

# Query para analisar quanto a produção de energia reflete na sua utilização

query = '''
SELECT
    Country,
    Year,
    SUM(CASE WHEN Power_is_renewable = TRUE THEN Power_Generation ELSE 0) AS Power_Renewable,
    Sum(CASE WHEN Power_is_renewable = FALSE THEN Power_Generation ELSE 0) AS POwer_Not_Renewable,
    Power_Consumed,
    Renewable_share_pct,
    Power_Import,
    Electricity
FROM info_pais
GROUP BY Country, Year, Power_Import, Electricity, Power_Consumed, Renewable_share_pct
ORDER BY Year DESC, Electricity DESC, Power_Renewable DESC, Power_Consumed DESC
'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    print(result.fetchdf())  # Converta para DataFrame pandas para melhor visualização
