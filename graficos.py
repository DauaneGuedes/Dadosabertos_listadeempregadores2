import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

print("Conectando ao banco de dados...")
engine = create_engine('postgresql+psycopg2://postgres:senha123@localhost:5432/Projeto_analista')

# 1. Fazendo a consulta direto no banco de dados usando SQL
query = """
    SELECT uf, COUNT(*) as quantidade 
    FROM lista_suja 
    GROUP BY uf 
    ORDER BY quantidade DESC 
    LIMIT 5;
"""
df_estados = pd.read_sql(query, engine)

print("Dados extraídos do banco! Desenhando o gráfico...")

# 2. Configurando o visual do gráfico (Modo Dark amigável)
plt.figure(figsize=(10, 6))
sns.set_theme(style="darkgrid") # Fundo escuro com grade, descansa a vista

# 3. Criando o gráfico de barras horizontais
grafico = sns.barplot(
    data=df_estados,
    x='quantidade',
    y='uf',
    palette='Reds_r' # Tons de vermelho profundo (combina com o tema "Lista Suja")
)

# 4. Adicionando os números na ponta de cada barra
for i in grafico.containers:
    grafico.bar_label(i, padding=5, fontsize=12, fontweight='bold', color='white')

# 5. Adicionando Títulos e Rótulos
plt.title('Top 5 Estados com Mais Registros de Trabalho Escravo', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Quantidade de Empregadores Autuados', fontsize=12)
plt.ylabel('Estado (UF)', fontsize=12)

# 6. Salvando a imagem na sua pasta e exibindo na tela
nome_imagem = 'grafico_top5_estados.png'
plt.savefig(nome_imagem, bbox_inches='tight')
print(f"✅ Sucesso! O arquivo '{nome_imagem}' foi salvo na sua pasta.")

plt.show() # Abre a janela com o gráfico final