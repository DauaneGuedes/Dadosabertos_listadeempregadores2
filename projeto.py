import pandas as pd
arquivo= "cadastro_de_empregadores.csv"
df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="cp1252"
)
print("Dimensões:", df.shape)

print("\nColunas:")
print(df.columns.tolist())

print("\nPrimeiros registros:")
print(df.head())
print("\nValores ausentes por coluna:")
print(df.isnull().sum())
print("Formato:", df.shape)

print("\nTipos de dados:")
print(df.dtypes)

print("\nValores ausentes:")
print(df.isnull().sum())

print("\nLinhas duplicadas:")
print(df.duplicated().sum())

print("\nAmostra:")
print(df.head(5).to_string())
# 1. Conferir os valores das colunas categóricas
for coluna in ["UF", "Decisão administrativa de procedência"]:
    print(f"\n--- Valores encontrados em {coluna} ---")
    print(df[coluna].value_counts(dropna=False).to_string())

# 2. Conferir os anos disponíveis
print("\n--- Anos da ação fiscal ---")
print(df["Ano da ação fiscal"].value_counts(dropna=False).sort_index())

# 3. Identificar datas que não podem ser interpretadas
for coluna in [
    "Decisão administrativa de procedência",
    "Inclusão no Cadastro de Empregadores"
]:
    datas = pd.to_datetime(
        df[coluna],
        format="%d/%m/%Y",
        errors="coerce"
    )

    invalidas = df[coluna].notna() & datas.isna()

    print(f"\n--- Datas inválidas: {coluna} ---")
    print("Quantidade:", invalidas.sum())
    print(df.loc[invalidas, coluna].to_string())

# 4. Verificar espaços no início ou no fim dos textos
print("\n--- Textos com espaços externos ---")
for coluna in df.select_dtypes(include=["str", "object"]).columns:
    textos = df[coluna].dropna().astype(str)
    quantidade = (textos != textos.str.strip()).sum()

    if quantidade:
        print(f"{coluna}: {quantidade}")