import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Guardando informações do arquivo na  variavel 'df' 
df = pd.read_csv('vgsales.csv')
# print(df.head())  # Verificando  se tabela esta sendo lida corretamente 
# print(df.info()) # verificar informações da tabela, para evitar erros em buscas por dados
# print(df.describe()) #Verificar informações sobre as vendas ds jogos para fazer a próxima parte do código
#quando executo o .describe() quero olhar para a coluna Global_Sales pois quero ver o jogo mais vendido.

top10MaisVendidos = df.sort_values(by ='Global_Sales', ascending = False).head(10)

#ascending = False serve para  deixar em ordem crescente 

print("Top 10 jogos mais vendidos:")

print(top10MaisVendidos[['Rank', 'Name','Platform','Year', 'Global_Sales']])

contagemPlataformas = df['Platform'].value_counts()
#value_counts conta quantas vezes um valor único aparece
print("\nPlataforma com mais jogos lançados:")
print(contagemPlataformas.head(1))

print("10 plataformas com mais jogos lançados:")
print(contagemPlataformas.head(10))

vendasGeneroPorRegiao = df.groupby('Genre')[['NA_Sales', 'JP_Sales']].sum()
#selecionando colunas de vendas 

generoMaisPopularNa = vendasGeneroPorRegiao.sort_values(by = 'NA_Sales', ascending = False)
genberoMaisPopularJp = vendasGeneroPorRegiao.sort_values(by = 'JP_Sales', ascending = False)

print("Gênero mais popular na América do Norte (em milhões de cópias):")
print(generoMaisPopularNa.head(1))

print("\nGênero mais popular no Japão (em milhões de cópias):")
print(genberoMaisPopularJp.head(1))

#---------------------------------------
#VIZUALIZAÇÃO DOS GRÁFICOS
#---------------------------------------

#1. top 10 jogos mais vendidos
sns.set_style('whitegrid')

# Definir o tamanho da tabela
plt.figure(figsize=(10, 6))

sns.barplot(x='Name',  y = 'Global_Sales', data = top10MaisVendidos)
#.barplot(x,y, data), criar um gráfico de barras

plt.title ('Top 10 jogos mais vendidos globalmente', fontsize = 16)#Título do gráfico
plt.xlabel('Jogo', fontsize = 12)
plt.ylabel('Vendas globais (Em milhões)', fontsize = 12)

plt.xticks(rotation = 45, ha ='right')

#Salvando imagem em um arquivo
plt.savefig('top_10_jogos.png', bbox_inches='tight')

print("\nGráfico dos 10 jogos mais vendidos foi salvo como 'top_10_jogos.png'")

#2. plataformas com mais jogos lançados

plt.figure( figsize=(6,10))

# selcionando as plataformas com mais jogos 
top10Plataformas = contagemPlataformas.head(10)

sns.barplot(x=top10Plataformas.index, y=top10Plataformas.values)
#Na direção x ficara o nome das plataformas e na y os valores de cada uma .

plt.title('Top 10 Plataformas com Mais Jogos Lançados', fontsize=16)
plt.xlabel('Plataforma', fontsize=12)
plt.ylabel('Quantidade de Jogos', fontsize=12)

plt.savefig('top_10_plataformas.png', bbox_inches='tight')
print("Gráfico das 10 plataformas com mais jogos foi salvo como 'top_10_plataformas.png'")

#3. Genêros dos jogos por região

topGenerosNa = generoMaisPopularNa.head(5)
topGenerosJp = genberoMaisPopularJp.head(5)

fig, axes = plt.subplots(1, 2, figsize=(15,6))# 1 linha, 2 colunas de gráficos

#Gráficos para o Na
sns.barplot(ax=axes[0], x=topGenerosNa.index, y=topGenerosNa.NA_Sales)
axes[0].set_title('Gêneros Mais Populares na América do Norte')
axes[0].set_ylabel('Vendas (em milhões)')
axes[0].set_xlabel('Gênero')

#Gráfico para o japão
sns.barplot(ax=axes[1], x=topGenerosJp.index, y=topGenerosJp.JP_Sales)
axes[1].set_title('Gêneros Mais Populares no Japão')
axes[1].set_ylabel('Vendas (em milhões)')
axes[1].set_xlabel('Gênero') 

plt.tight_layout()#Servepara o layout não ficar apertado e salavar a imagem,  pois quando tentei a imagem não caregou corretamente
plt.savefig('top_generos_regiao.png')

print("Gráfico comparativo de gêneros por região foi salvo como 'top_generos_regiao.png'")