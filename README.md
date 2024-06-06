# Project-Marketing
O código realiza uma análise abrangente de dados de leads, compradores, personas e anúncios, fornecendo insights valiosos sobre o desempenho de campanhas e características dos leads e compradores. Utiliza bibliotecas como pandas para manipulação de dados, matplotlib e seaborn para visualização.

Passos Realizados
Carregamento dos Dados:

Os dados são carregados de quatro arquivos CSV utilizando pandas.
Arquivos carregados: TabelaPesquisaUTMsn.csv, TabelaVendas.csv, TabelaPesquisa.csv, TabelaAdsLinks.csv.
Visualização Inicial dos Dados:

Impressão das primeiras linhas de cada tabela para entender a estrutura dos dados.
Análise da Primeira Tabela (Leads Inscritos):

Cálculo do total de leads únicos.
Contagem de leads por canal de origem (utmsource), por anúncio (utmterm) e por público (utmmedium).
Análise da Segunda Tabela (Compradores):

Cálculo do total de compradores únicos.
Identificação de leads que se tornaram compradores.
Cálculo da taxa de conversão geral e por canal de origem, anúncio e público.
Análise da Terceira Tabela (Pesquisa de Persona):

Identificação de personas que são compradores.
Distribuição de leads por faixa etária, faixa de renda e tempo de conhecimento.
Cálculo da taxa de conversão por faixa etária, faixa de renda e tempo de conhecimento.
Análise da Quarta Tabela (Anúncios):

Identificação dos anúncios (utmterm) com melhor taxa de conversão.
Extração das URLs dos anúncios com melhor desempenho.
Visualização dos Dados:

Definição de uma função para plotar gráficos de barras.
Criação de gráficos para:
Distribuição de leads por canal de origem, anúncio e público.
Taxa de conversão por canal de origem, anúncio e público.
Distribuição de leads por faixa etária, faixa de renda e tempo de conhecimento.
Taxa de conversão por faixa etária, faixa de renda e tempo de conhecimento.
Exibição dos Resultados em Tabelas:

Impressão dos resultados das análises, incluindo distribuições e taxas de conversão.
Resultado Esperado
O código fornece uma visão detalhada do comportamento dos leads e compradores, permitindo identificar quais campanhas e anúncios são mais eficazes e entender melhor as características dos leads que convertem em compradores.
