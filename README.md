# Second_Project_DuckDB

**Autores:**  
- Ana Beatriz Hidalgo  
- André Lucas Loubet Souza

**Disciplina:** MC536 – Banco de Dados (Unicamp, 1º semestre 2025)  
**Tema:** Transformar o banco de dados feito no primeiro projeto em um banco tabelar usando o Duck DB, por causa do cenario que nos foi atribuido.

## 🔍 Sobre

Este projeto foi desenvolvido como continuação do primeiro trabalho desenvolvido na disciplina MC536 – Banco de Dados da Unicamp, primeiro semestre de 2025, em que nosso banco deveria ser reconfigurado para atender as exigencias do cenário atribuido a nos.

Link do trabalho anterior para contextualização: https://github.com/AnaBeatrizHidalgo/First-Database-

**Cenário:**  
Você foi contratado para reformular um sistema de consulta a dados altamente estruturados. As principais operações consistem em realizar análises estatísticas sobre grandes volumes de dados históricos e imutáveis. As consultas acessam frequentemente um número pequeno de atributos, mas um número grande de registros. O sistema é utilizado por analistas de dados que preferem uma integração direta com linguagens como Python ou R.

Requisitos Técnicos:
- Predominância de operações de leitura e agregação sobre grandes datasets.
- Alta compressão e performance em operações de leitura.
- Baixa frequência de escrita ou atualização.
- Integração com notebooks ou scripts de análise.
- Confiabilidade em leituras, mas sem exigência de controle transacional complexo.

## Sumário

[Objetivos](#objetivos)  
[Estrutura do Repositório](#estrutura-do-repositório)  
[Tecnologias Utilizadas](#tecnologias-utilizadas)
[Configuração e Execução](#configuração-e-execução)  
[Modelagem de Dados](#modelagem-de-dados)  
[População do Banco](#população-do-banco)  
[Consultas SQL](#consultas-sql)  

## ✅ Objetivos

- Modelo logico com os  dados utilizados no projeto anterior.
- Criar script com modelo físico e população dos dados.
- Desenvolver consultas SQL para extrair insights relevantes.

## 📂 Estrutura do Repositório
```
Second_Project_DuckDB/
├── Consultas/ # Arquivos com consultas pré-definidas
├── Datasets/ # Conjuntos de dados brutos (CSV, etc.)
├── bancoDuck.py # Script com o modelo físico e a população dos dados
├── Modelo Logico.png # Imagem ilustando o modelo lógico
├── project.db # Banco de dados em si
└── README.md
```

## 🛠️ Tecnologias Utilizadas

1. **Python 3.8+** e **pip**.

## 🚀 Configuração e Execução

1. **Clone o repositório:**
```
git clone https://github.com/AnaBeatrizHidalgo/Second_Project_DuckDB
cd First-Database-
```

2. Instale dependências:
```
pip install duckdb
```

3. Execute o script de população:
```
python bancoDuck.py
```

## 📈 Modelagem de Dados

- `Logico.png` - Modelo Lógico (relacional)
![Visão do Modelo Logico](/Modelo%20Logico.png)

## 📊 População do Banco

O script `/bancoDuck.py`:

    Conecta  usando connect do Duckdb por meio do arquivo project.db

    Que se ainda não existir o proprio script cria

    Cria esquemas e tabelas (se ainda não existirem).

    Insere dados a partir dos CSVs em `Datasets/`.

## 📄 Consultas SQL

As consultas em SQL foram encapsuladas em Python.

Em `Consultas/ estão as consultas mais relevantes para análise, por exemplo:

- `/firstQuery.py`

- `/secondQuery.py`

- `/thirdQuery.py`

- `/fourthQuery.py`

- `/fifthQuery.py`
