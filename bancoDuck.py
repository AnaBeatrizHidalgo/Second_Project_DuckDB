import duckdb

# Conexão com o banco
con = duckdb.connect("project.db")

# Recria sempre a tabela info_pais para garantir dados atualizados
print("Recriando tabela info_pais...")
con.execute("DROP TABLE IF EXISTS info_pais")

con.execute('''
    CREATE TABLE info_pais (
        Country VARCHAR,
        Year INTEGER,
        Population BIGINT,
        IDH FLOAT,
        Electricity FLOAT,
        Sanitation FLOAT,
        Health FLOAT,
        Standard_Living FLOAT,
        GDP FLOAT,
        Eletricity_Investimente FLOAT,
        Health_Investimente FLOAT,
        CO2_Emission_Total FLOAT,
        Power_Consumed FLOAT,
        Renewable_share_pct FLOAT,
        Power_Import FLOAT,
        Sector VARCHAR,
        CO2_Emission_Sector FLOAT,
        Power_Source VARCHAR,
        Power_is_renewable BOOLEAN,
        Power_Generation FLOAT,
        CO2_Emission_Power FLOAT
    )
''')

# Leitura correta do CSV
con.execute("""
    CREATE TEMP TABLE temp_csv AS 
    SELECT * FROM read_csv_auto('./Datasets/DadosCompletos.csv', HEADER=TRUE)
""")

# Inserção com os nomes corretos
con.execute("""
    INSERT INTO info_pais
    SELECT
        Country,
        Year,
        Population,
        IDH,
        Electricity,
        Sanitation,
        Health,
        Standard_Living,
        GDP,
        Investment_Energy     AS Eletricity_Investimente,
        Health_Expenditure    AS Health_Investimente,
        CO2_Emission_Total,
        Power_Consumed,
        Renewble_Energy       AS Renewable_share_pct,
        Power_Import,
        Sector,
        CO2_Emission_Sector,
        Power_Source,
        Power_is_renewable,
        Power_Generation,
        CO2_Emission_Power
    FROM temp_csv
""")

# Verificação simples
df = con.execute("SELECT Country, Year, IDH, GDP FROM info_pais LIMIT 100").fetchdf()
print("\nPrévia dos dados após recarga:")
print(df)

con.close()
