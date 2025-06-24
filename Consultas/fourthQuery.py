import duckdb

# Query com as informações de emissão de CO2 globalmente,  extraindo o pais, o sector e a energia que mais emitem CO2

query = '''
WITH sector_emissions AS (
    SELECT
        year,
        SUM(co2_emission_sector)                   AS co2_total_sector,
        arg_max(sector, co2_emission_sector)       AS sector_maior_emissao
    FROM info_pais
    GROUP BY year
),
energy_emissions AS (
    SELECT
        year,
        SUM(co2_emission_power)                    AS co2_total_energia,
        arg_max(power_source, co2_emission_power)  AS energia_maior_emissao
    FROM info_pais
    GROUP BY year
),
country_emissions AS (
    SELECT
        year,
        SUM(co2_emission_total)                    AS co2_total_country,
        arg_max(country, co2_emission_total)       AS country_maior_emissao
    FROM info_pais
    GROUP BY year
),
idh_totals AS (
    SELECT
        year,
        SUM(idh)                                   AS total_idh
    FROM info_pais
    GROUP BY year
),
gdp_totals AS (
    SELECT
        year,
        SUM(gdp)                                   AS total_gdp
    FROM info_pais
    GROUP BY year
)

SELECT
    se.year,
    se.co2_total_sector,
    se.sector_maior_emissao,
    ee.co2_total_energia,
    ee.energia_maior_emissao,
    ce.co2_total_country,
    ce.country_maior_emissao,
    it.total_idh,
    gt.total_gdp
FROM       sector_emissions  se
JOIN       energy_emissions  ee USING (year)
JOIN       country_emissions ce USING (year)
JOIN       idh_totals        it USING (year)
JOIN       gdp_totals        gt USING (year)
ORDER BY   ce.co2_total_country DESC,
           ee.co2_total_energia DESC,
           se.co2_total_sector DESC
LIMIT 10;

'''

with duckdb.connect("project.db") as con:
    result = con.execute(query)
    df = result.fetchdf()
    df.to_csv("./Consultas/queryFourth.csv", index=False)  # Salva em CSV sem incluir o índice
    print(df)                                 # Printar no terminal
