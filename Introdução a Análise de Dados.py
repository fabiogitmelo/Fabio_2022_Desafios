#Desafio:
#Empresa Vende Bermudas
#5 Lojas
#Está querendo aumentar as vendas
#O que fazer?
#Informações Disponíveis: Base de Vendas

#Passo 1 - Trazer sua base de dados para o Python e ver o que tem nela
import pandas as pd

tabela = pd.read_excel("Vendas_2.xlsx")
display(tabela)# É um print de forma estilizda

#Passo 2 - Pegar um panorama geral sobre a sua base de dados
#Criando nova variável (Calculando Faturamento da empresa)

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

#Passo 3 - Começar sua análise Top -> Dow
## Calculando Faturamento por loja

faturamento_por_loja = tabela[["ID Loja", "Valor Final"]]
display(faturamento_por_loja)

#Calculando Faturamento por loja agrupando por loja e somando os valores de cada l9ja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamento_por_loja)

#Passo 4 - Entrar no detalhe para entender
#Calculando Faturamento por produto
faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_por_produto)

