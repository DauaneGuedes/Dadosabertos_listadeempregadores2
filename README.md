Análise de Dados Abertos — Trabalho Análogo à Escravidão

Sobre o projeto

Projeto de análise exploratória de dados públicos disponibilizados pelo Governo Federal, com foco nos registros de empregadores autuados por submeter trabalhadores a condições análogas à escravidão.

O objetivo é explorar os dados, identificar padrões e construir visualizações que facilitem a compreensão das informações.

Fonte dos dados

Portal: Portal Brasileiro de Dados Abertos

Conjunto de dados: Trabalho Análogo ao de Escravo

Tecnologias utilizadas

Python

Pandas

Matplotlib

Seaborn

CSV

Git e GitHub

Etapas da análise

Carregamento e leitura da base de dados em formato CSV.

Inspeção da estrutura, das colunas e dos tipos de dados.

Verificação de valores ausentes e registros duplicados.

Análise das atividades econômicas mais recorrentes.

Identificação dos cinco estados com maior quantidade de registros.

Construção de gráficos para explorar a distribuição dos dados e sua evolução temporal.

Visualizações

O projeto inclui gráficos para facilitar a interpretação dos resultados:

Evolução temporal: visualização da quantidade de registros ao longo dos anos.

Principais estados: comparação dos cinco estados com maior número de registros.

Atividades econômicas: análise das três atividades mais recorrentes.

As imagens dos gráficos estão disponíveis nos arquivos grafico_evolucao_anos.png e grafico_top5_estados.png. Os scripts de visualização estão disponíveis em graficos.py e grafico_temporal.py.

Estrutura do projeto

projeto.py — leitura e inspeção inicial dos dados.

analise.py — análise exploratória da base.

graficos.py — geração de visualizações.

grafico_temporal.py — análise gráfica da evolução temporal.

cadastro_de_empregadores.csv — arquivo de dados utilizado na análise.

Objetivo de aprendizagem

Aplicar conceitos de análise exploratória de dados com Python, praticando manipulação de dados, identificação de padrões e comunicação de resultados por meio de visualizações.

Observação

Este projeto tem finalidade educacional e utiliza dados públicos. Os resultados dependem da versão da base analisada e dos critérios de tratamento e seleção aplicados.
