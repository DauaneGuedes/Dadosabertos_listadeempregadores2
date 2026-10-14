import pandas as pd
# 1. LEITURA DOS DADOS
arquivo = "cadastro_de_empregadores.csv"
df = pd.read_csv(arquivo, sep=";", encoding="cp1252")

print("Dados carregados com sucesso! Iniciando limpeza...\n")

# 2. LIMPEZA DOS DADOS
# Remove espaços invisíveis de todas as colunas de texto de uma vez só
colunas_texto = df.select_dtypes(include=["str", "object"]).columns
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip()

# Padroniza a coluna UF para garantir que tudo fique em maiúsculo (ex: 'rj' vira 'RJ')
if "UF" in df.columns:
    df["UF"] = df["UF"].str.upper()

# 3. EXTRAINDO INSIGHTS SOCIAIS
print("="*50)
print(" RELATÓRIO: PANORAMA DO TRABALHO ESCRAVO")
print("="*50)

# Pergunta 1: Quais estados têm os maiores índices de flagrantes?
print("\n📍 TOP 5 Estados com mais registros na 'Lista Suja':")
top_estados = df["UF"].value_counts().head(5)
print(top_estados.to_string())

# Pergunta 2: Como foi a evolução dessas ações de fiscalização ao longo dos anos?
if "Ano da ação fiscal" in df.columns:
    print("\n📅 Evolução das Ações Fiscais por Ano:")

    # CORREÇÃO: Força a coluna a ser número inteiro, ignorando os vazios
    df["Ano da ação fiscal"] = df["Ano da ação fiscal"].astype('Int64')

    acoes_por_ano = df["Ano da ação fiscal"].value_counts().sort_index()
    print(acoes_por_ano.to_string())

# Pergunta 3: Qual setor (CNAE) explora mais?
colunas_cnae = [c for c in df.columns if "CNAE" in c.upper() or "ATIVIDADE" in c.upper()]
if colunas_cnae:
    nome_col_cnae = colunas_cnae[0]
    print(f"\n🏢 TOP 3 Setores Econômicos com mais casos (Coluna: {nome_col_cnae}):")

    top_setores = df[nome_col_cnae].value_counts().head(3)
    # CORREÇÃO: Tirei o 'index=False' para ele mostrar o nome do setor junto com a quantidade!
    print(top_setores.to_string())
    from sqlalchemy import create_engine

    print("\nPreparando o envio para o PostgreSQL...")

    df_banco = df.rename(columns={
        "Empregador": "empregador",  # <-- Troque "Empregador" pelo nome exato que o governo usou
        "CNPJ/CPF": "cnpj_cpf",  # <-- Verifique se está exatamente "CNPJ/CPF"
        "UF": "uf",
        "CNAE": "cnae",  # <-- Verifique se é "CNAE", "Codigo CNAE", etc.
        "Ano da ação fiscal": "ano_acao"
    })

    colunas_selecionadas = ["empregador", "cnpj_cpf", "uf", "cnae", "ano_acao"]
    df_banco = df_banco[colunas_selecionadas]

    # 2. Criando a conexão
    # Formato: postgresql+psycopg2://usuario:senha@localhost:porta/nome_do_banco
    engine = create_engine('postgresql+psycopg2://postgres:senha123@localhost:5432/Projeto_analista')

    # 3. O comando mágico: envia o DataFrame direto para a tabela
    df_banco.to_sql('lista_suja', engine, if_exists='append', index=False)

    print("🚀 Dados inseridos com sucesso no PostgreSQL!")