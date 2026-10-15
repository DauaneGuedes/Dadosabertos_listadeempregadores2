import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

print("Conectando ao banco de dados para buscar a linha do tempo...")
engine = create_engine('postgresql+psycopg2://postgres:senha123@localhost:5432/Projeto_analista')

# 1. Consulta SQL agrupando e ordenando por ano
query = """
    SELECT ano_acao, COUNT(*) as quantidade 
    FROM lista_suja 
    WHERE ano_acao IS NOT NULL
    GROUP BY ano_acao 
    ORDER BY ano_acao ASC;
"""
df_anos = pd.read_sql(query, engine)

print("Dados temporais extraídos! Desenhando o gráfico de linha...")

# 2. Configurando o visual do gráfico (Modo Dark amigável e fontes grandes)
plt.figure(figsize=(12, 6))
sns.set_theme(style="darkgrid")

# 3. Criando o gráfico de linha
grafico = sns.lineplot(
    data=df_anos,
    x='ano_acao',
    y='quantidade',
    color='#e74c3c',   # Vermelho claro para contrastar com o fundo escuro
    linewidth=4,       # Linha bem grossa para facilitar a visualização
    marker='o',        # 'o' cria bolinhas em cada ano
    markersize=12      # Tamanho grande para as bolinhas
)

# 4. Adicionando os números exatamente em cima de cada bolinha
for index, row in df_anos.iterrows():
    grafico.text(
        row['ano_acao'],
        row['quantidade'] + 5, # Sobe um pouquinho o texto para não encostar na bolinha
        f"{row['quantidade']}",
        color='white',
        ha="center",
        fontweight='bold',
        fontsize=12
    )

# 5. Adicionando Títulos e Rótulos (Acessibilidade visual)
plt.title('Evolução das Ações de Combate ao Trabalho Escravo', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Ano da Ação Fiscal', fontsize=14)
plt.ylabel('Quantidade de Empregadores', fontsize=14)

# Garante que todos os anos apareçam no eixo X como números inteiros
plt.xticks(df_anos['ano_acao'])

# 6. Salvando e exibindo
nome_imagem = 'grafico_evolucao_anos.png'
plt.savefig(nome_imagem, bbox_inches='tight')
print(f"✅ Sucesso! O arquivo '{nome_imagem}' foi salvo.")

plt.show()