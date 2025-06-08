import duckdb

#Conexão com o banco
con = duckdb.connect("project.db")

# Creating the colunar table
info_pais = con.sql('''
    CREATE TABLE info_pais 
        (Country VARCHAR,
         Year INTEGER,
         Population INTEGER,
         IDH NUMERICAL,
         Eletricity NUMERICAL,
         Sanitation NUMERICAL,
         Life_expectancy  NUMERICAL,
         GDP NUMERICAL,
         Eletricity_Investimente NUMERICAL,
         Health_Investimente NUMERICAL,
         CO2_Emission_Total NUMERICAL,
         Power_Consumed NUMERICAL,
         Power_Import NUMERICAL,
         Renewble_Energy NUMERICAL,
         Sector VARCHAR,
         Sector_Descrition VARCHAR,
         CO2_Emission_Sector NUMERICAL,
         Power_Source VARCHAR,
         Power_is_renewable  BOOLEAN,
         Power_Generation NUMERICAL,
         CO2_Emission_Power NUMERICAL,
                       )''')

# Importing a CSV file to in-memory database
con.sql("SELECT info_pais, COUNT(*) " \
           "FROM read_csv('nosso.csv') " \
           "WHERE info_pais IS NOT NULL " \
           "GROUP BY info_pais " \
           "ORDER BY info_pais").show()


