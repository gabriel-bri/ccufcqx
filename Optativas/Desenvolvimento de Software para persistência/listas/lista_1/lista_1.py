# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Lista 1
# Importando dados
!wget https://raw.githubusercontent.com/pinheirovictor/2024.2_QXD0099_persistencia-02A/refs/heads/main/vendas.csv

# Carregar o CSV: Leia o arquivo vendas.csv para um DataFrame usando pandas.
df = pd.read_csv("vendas.csv")

df

# Crie uma nova coluna chamada Total_Venda, que representa o valor total de cada venda (Quantidade * Preço_Unitário).
df['Total_Vendas'] = df['Quantidade'] * df['Preco_Unitario']

df

# Agrupe os dados por Produto e calcule o total de vendas para cada produto.
total_vendas = df.groupby('Produto')['Total_Vendas'].sum()
total_vendas

# Filtre as vendas do mês de janeiro (1) de 2023.
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
vendas_janeiro = df[(df['Data'].dt.month == 1) & (df['Data'].dt.year == 2023)]
vendas_janeiro

# Crie um DataFrame separado com esses dados.
vendas_janeiro.to_csv('vendas_janeiro.csv')

# Salvar o total de vendas por produto em uma nova planilha Excel
total_vendas = total_vendas.reset_index()

with pd.ExcelWriter('total_vendas_produto.xlsx', engine='openpyxl') as writer:
    for _, row in total_vendas.iterrows():
        produto = row['Produto']
        total = row['Total_Vendas']

        # Criar um DataFrame para o produto
        dados_produto = pd.DataFrame({
            'Produto': [produto],
            'Total_Vendas': [total]
        })

        # Salvar cada produto em uma aba
        dados_produto.to_excel(writer, sheet_name=produto, index=False)

plt.figure(figsize=(10, 6))
plt.bar(total_vendas['Produto'], total_vendas['Total_Vendas'], color='skyblue')
plt.title('Vendas Totais por Produto', fontsize=16)
plt.xlabel('Produto', fontsize=14)
plt.ylabel('Total de Vendas', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()