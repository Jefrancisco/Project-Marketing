import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados das planilhas
leads_df = pd.read_csv('Arquivos\TabelaPesquisaUTMsn.csv')
compradores_df = pd.read_csv('Arquivos\TabelaVendas.csv')
persona_df = pd.read_csv('Arquivos\TabelaPesquisa.csv')
ads_df = pd.read_csv('Arquivos\TabelaAdsLinks.csv')

print(leads_df.head())
print(compradores_df.head())
print(persona_df.head())
print(ads_df.head())

# 1. Análise da Primeira Tabela (Leads Inscritos)
total_leads = leads_df['email'].nunique()
leads_by_source = leads_df['utmsource'].value_counts()
leads_by_term = leads_df['utmterm'].value_counts()
leads_by_medium = leads_df['utmmedium'].value_counts()

# 2. Análise da Segunda Tabela (Compradores)
total_compradores = compradores_df['email'].nunique()
leads_df['comprador'] = leads_df['email'].isin(compradores_df['email'])
taxa_conversao_geral = (total_compradores / total_leads) * 100

conversao_por_source = leads_df.groupby('utmsource')['comprador'].mean() * 100
conversao_por_term = leads_df.groupby('utmterm')['comprador'].mean() * 100
conversao_por_medium = leads_df.groupby('utmmedium')['comprador'].mean() * 100

# 3. Análise da Terceira Tabela (Pesquisa de Persona)
persona_df['comprador'] = persona_df['email'].isin(compradores_df['email'])

distribuicao_idade = persona_df['idade'].value_counts()
distribuicao_renda = persona_df['renda'].value_counts()
distribuicao_tempo = persona_df['tempo_me_conhece'].value_counts()

conversao_por_idade = persona_df.groupby('idade')['comprador'].mean() * 100
conversao_por_renda = persona_df.groupby('renda')['comprador'].mean() * 100
conversao_por_tempo = persona_df.groupby('tempo_me_conhece')['comprador'].mean() * 100

# 4. Análise da Quarta Tabela (Anúncios)
top_ads_terms = conversao_por_term[conversao_por_term > 0].index
top_ads_df = ads_df[ads_df['utmterm'].isin(top_ads_terms)]
top_ads_urls = top_ads_df['instagram_permalink_url'].tolist()

# Função para plotar gráficos
def plot_bar(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data.values, y=data.index, palette='viridis')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Plotando gráficos
plot_bar(leads_by_source, 'Distribuição de Leads por Canal de Origem', 'Quantidade de Leads', 'Canal de Origem')
plot_bar(leads_by_term.head(10), 'Top 10 Anúncios por Quantidade de Leads', 'Quantidade de Leads', 'Anúncio (UTM Term)')
plot_bar(leads_by_medium.head(10), 'Top 10 Públicos por Quantidade de Leads', 'Quantidade de Leads', 'Público (UTM Medium)')

plot_bar(conversao_por_source, 'Taxa de Conversão por Canal de Origem', 'Taxa de Conversão (%)', 'Canal de Origem')
plot_bar(conversao_por_term.head(10), 'Top 10 Anúncios por Taxa de Conversão', 'Taxa de Conversão (%)', 'Anúncio (UTM Term)')
plot_bar(conversao_por_medium.head(10), 'Top 10 Públicos por Taxa de Conversão', 'Taxa de Conversão (%)', 'Público (UTM Medium)')

plot_bar(distribuicao_idade, 'Distribuição de Leads por Faixa Etária', 'Quantidade de Leads', 'Faixa Etária')
plot_bar(distribuicao_renda, 'Distribuição de Leads por Faixa de Renda', 'Quantidade de Leads', 'Faixa de Renda')
plot_bar(distribuicao_tempo, 'Distribuição de Leads por Tempo de Conhecimento', 'Quantidade de Leads', 'Tempo de Conhecimento')

plot_bar(conversao_por_idade, 'Taxa de Conversão por Faixa Etária', 'Taxa de Conversão (%)', 'Faixa Etária')
plot_bar(conversao_por_renda, 'Taxa de Conversão por Faixa de Renda', 'Taxa de Conversão (%)', 'Faixa de Renda')
plot_bar(conversao_por_tempo, 'Taxa de Conversão por Tempo de Conhecimento', 'Taxa de Conversão (%)', 'Tempo de Conhecimento')

# Exibir resultados em tabelas
print("Total de Leads:")
print(total_leads)
print("\nDistribuição por Canal de Origem:")
print(leads_by_source)
print("\nDistribuição por Anúncio:")
print(leads_by_term.head(10))
print("\nDistribuição por Público:")
print(leads_by_medium.head(10))

print("\nDistribuição por Faixa Etária:")
print(distribuicao_idade)
print("\nDistribuição por Faixa de Renda:")
print(distribuicao_renda)
print("\nDistribuição por Tempo de Conhecimento:")
print(distribuicao_tempo)

print("\nTaxa de Conversão por Faixa Etária:")
print(conversao_por_idade)
print("\nTaxa de Conversão por Faixa de Renda:")
print(conversao_por_renda)
print("\nTaxa de Conversão por Tempo de Conhecimento:")
print(conversao_por_tempo)

print("\nURLs dos Anúncios com Melhor Performance:")
for url in top_ads_urls:
    print(url)

