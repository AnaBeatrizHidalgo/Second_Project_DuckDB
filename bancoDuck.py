import duckdb

# Conexão com o banco
con = duckdb.connect("project.db")

# Lista todas as tabelas disponíveis
tables = con.execute("SHOW TABLES").fetchall()
print("Tabelas no banco:", tables)

# Se info_pais não existir, crie-a
if not any('info_pais' in table for table in tables):
    print("Criando tabela info_pais...")
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

    # Crie uma tabela temporária
    con.execute("""
        CREATE TEMP TABLE temp_csv AS 
        SELECT * FROM read_csv('./Datasets/DadosCompletos.csv', AUTO_DETECT=TRUE)
    """)

    # Insira apenas as colunas desejadas
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
            Investment_Energy AS Eletricity_Investimente,
            Health_Expenditure AS Health_Investimente,
            CO2_Emission_Total,
            Power_Consumed,
            Power_Import,
            Renewble_Energy,
            Sector,
            CO2_Emission_Sector,
            Power_Source,
            Power_is_renewable,
            Power_Generation,
            CO2_Emission_Power
        FROM temp_csv
    """)

# Verificando se popular os dados deu certo
result = con.sql("SELECT * FROM info_pais LIMIT 5")
print(result)
con.close()
