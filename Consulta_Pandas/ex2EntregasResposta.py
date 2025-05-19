# -*- coding: utf-8 -*-
"""
Respostas completas para ex2EntregasTemplate.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar as Series
srValor = pd.read_excel('meio_bairro_valor_Entrega.xlsx',
                        header=0, usecols=(0,2), index_col=0).squeeze("columns")
srDest = pd.read_excel('meio_bairro_valor_Entrega.xlsx',
                       header=0, usecols=(0,1), index_col=0).squeeze("columns")

print('\n-- Series valores das entregas --')
print(srValor)
print('\n-- Series destinos das entregas --')
print(srDest)

# 1- Tamanho
print('\n1- Tamanho:')
print(srValor.size)

# 2- 4 primeiros
print('\n2- 4 primeiros:')
print(srValor.head(4))

# 3- 4 últimos
print('\n3- 4 últimos:')
print(srValor.tail(4))

# 4- Quantos válidos (sem NaN)
print('\n4- Quantos válidos:')
print(srValor.count())

# 5- Exibir sem valores inválidos (sem alterar)
print('\n5- Series sem NaN:')
print(srValor.dropna())

# 6- Descartar valores inválidos (inplace)
print('\n6- Descartar NaN (inplace):')
srValor.dropna(inplace=True)
print(srValor)

# 7- Ordenar por índice (sem alterar)
print('\n7- Ordenada por índice (sem alterar):')
print(srValor.sort_index())

# 8- Ordenada decrescentemente por valor (sem alterar)
print('\n8- Ordenada decrescente por valor (sem alterar):')
print(srValor.sort_values(ascending=False))

# 9- Cópia da Series
print('\n9- Criando cópia:')
srCopia = srValor.copy()
print(srCopia)

# 10- Ordenar a cópia crescente por valor
print('\n10- Cópia ordenada crescente por valor:')
print(srCopia.sort_values(ascending=True))

# 11- Valores via VEICULO PROPRIO
print('\n11- Entregas via VEICULO PROPRIO:')
print(srValor.loc['VEICULO PROPRIO'])

# 12- Valores via MOTOBOY ou BICICLETA
print('\n12- Entregas via MOTOBOY ou BICICLETA:')
print(srValor.loc[['MOTOBOY','BICICLETA']])

# 13- Todos os valores desconsiderando RETIRADAS
print('\n13- Sem RETIRADA:')
print(srValor.drop(labels='RETIRADA', errors='ignore'))

# 14- Total geral
print('\n14- Total geral:')
print(srValor.sum())

# 15- Maior valor de entrega
print('\n15- Maior valor:')
print(srValor.max())

# 16- Meio de entrega do maior valor (e possíveis empates)
print('\n16- Método de entrega com maior valor:')
max_val = srValor.max()
print(srValor[srValor == max_val].index.tolist())

# 17- Valor médio das entregas
print('\n17- Valor médio:')
print(srValor.mean())

# 18- Valor médio via MOTOBOY
print('\n18- Valor médio MOTOBOY:')
print(srValor[srDest == 'MOTOBOY'].mean())

# 18b- Valor mais frequente (moda)
print('\n18b- Valor mais frequente:')
print(srValor.mode()[0])

# 19- Valores com 2 casas decimais e R$
print('\n19- Valores formatados:')
print(srValor.map(lambda x: f"R$ {x:.2f}"))

# 20- Valores líquidos descontando imposto
def detImposto(val, pa, pb):
    if val <= 25:
        return val
    elif val <= 100:
        return val*(1-pa/100)
    else:
        return val*(1-pb/100)

pa = 5  # exemplo 5%
pb = 10 # exemplo 10%
print('\n20- Valores líquidos (pa=5%, pb=10%):')
srLiquido = srValor.apply(lambda v: detImposto(v, pa, pb))
print(srLiquido)

# 21- Dividir valores em 3 faixas iguais
print('\n21- Faixas em 3 bins:')
srFaixas = pd.cut(srValor, bins=3)
print(srFaixas)

# 22- Faixas personalizadas com labels
print('\n22- Faixas personalizadas:')
bins = [0,40,100,300,srValor.max()]
labels = ['BARATA','REGULAR','CARA','EXAGERADA']
srCat = pd.cut(srValor, bins=bins, labels=labels)
print(srCat)

# 23a- Tabela de frequência absoluta de categorias
print('\n23a- Frequência absoluta de categorias:')
srTabFreqCat = srCat.value_counts()
print(srTabFreqCat)

# 23b- Frequência absoluta ordenada (labels)
print('\n23b- Frequência absoluta (ordenada):')
print(srTabFreqCat.reindex(labels))

# 23c- Frequência relativa (%)
print('\n23c- Frequência relativa (%):')
print(srCat.value_counts(normalize=True).reindex(labels)*100)

# 23d- Frequência de destinos
print('\n23d- Frequência de destinos:')
print(srDest.value_counts())

# 24- Cada meio de entrega uma única vez
print('\n24- Meios de entrega únicos:')
print(srDest.index.unique())

# 25- Quantos meios de entrega distintos
print('\n25- Quantidade de meios distintos:')
print(srDest.index.unique().size)

# 27- Tabela de frequência do índice (meios)
print('\n27- Freq do índice (meios):')
print(srDest.index.value_counts())

# 28- Meio de entrega mais utilizado
print('\n28- Meio mais utilizado:')
print(srDest.index.value_counts().idxmax())

# 29- Meio de entrega com menor valor
print('\n29- Meio com menor valor:')
print(srValor.idxmin())

# 30- Gráfico de barras de srValor
print('\n30- Gráfico de barras de valores:')
srValor.plot(kind='bar')
plt.show()

# 31- Gráfico de barras de srCat
print('\n31- Gráfico de barras de categorias:')
srCat.value_counts().plot(kind='bar')
plt.show()

# 32- Gráfico de pizza de srCat
print('\n32- Gráfico de pizza de categorias:')
srCat.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

# 33- Gráfico de barras de frequência dos meios
print('\n33- Gráfico de barras de meios:')
srDest.index.value_counts().plot(kind='bar')
plt.show()

# 34- Gráfico de pizza de frequência dos meios
print('\n34- Gráfico de pizza de meios:')
srDest.index.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

# 35- Quantidade de entregas por transporte
print('\n35- Quantidade de entregas por transporte:')
print(srDest.groupby(level=0).size())

# 36- Total, maior e menor valor por transporte
print('\n36- Total, Maior e Menor valor por transporte:')
print(srValor.groupby(level=0).agg(['sum','max','min']))

# 38- Quantidade de entregas por destino
print('\n38- Quantidade de entregas por destino:')
print(srDest.value_counts())

# 41- Média e Mediana de valor por categoria de preço
print('\n41- Média e Mediana por categoria:')
print(srValor.groupby(srCat).agg(['mean','median']))

# 42- (exemplo de crosstab) - categorias vs transporte
print('\n42- Categorias x transporte (crosstab):')
print(pd.crosstab(srCat, srValor.index))

# 43a- Meio x destino quantidades
print('\n43a- Meio x destino (quantidades):')
print(pd.crosstab(srValor.index, srDest))

# 43b- Meio x destino (valor total)
print('\n43b- Meio x destino (valor total):')
print(pd.crosstab(srValor.index, srDest, values=srValor, aggfunc='sum'))

# 44- Valor total por categoria x destino
print('\n44- Total por categoria x destino:')
print(pd.crosstab(srCat, srDest, values=srValor, aggfunc='sum').fillna(0))
