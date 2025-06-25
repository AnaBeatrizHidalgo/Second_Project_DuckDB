import duckdb

# O intuito dessa query é fazer a anlise de emissão de CO2
# Conseguindo fazer uma comparação entre a emissão total do pais, do setor e da energia, 
# em quem mais contribui para cada um

query = '''
SELECT
    year,
    SUM(co2_emission_total)                    AS co2_total_country,
    arg_max(country, co2_emission_total)       AS country_maior_emissao,
    SUM(co2_emission_sector)                   AS co2_total_sector,
    arg_max(sector, co2_emission_sector)       AS sector_maior_emissao,
    SUM(co2_emission_power)                    AS co2_total_energia,
    arg_max(power_source, co2_emission_power)  AS energia_maior_emissao
FROM info_pais
GROUP BY year
ORDER BY year DESC, co2_total_country DESC, co2_total_energia DESC, co2_total_sector DESC
LIMIT 10;

'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/queryFourth.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
