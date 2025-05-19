# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:26:01 2024

@author: Ferlin
"""

# -*- coding: latin-1 -*-  
############################################################################################
# Nome completo:
# Matrícula PUC-Rio:
# Declaração de autoria: Declaro que este documento foi produzido por mim em sua totalidade,
#                 sem consultas a outros alunos, professores ou qualquer outra pessoa.
############################################################################################

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Carregando dados do arquivo 'dados_lazer.xlsx'

srGeneroLiterario = pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0,1), index_col=0).squeeze('columns')
srIdade = pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0, 2), index_col=0).squeeze('columns')
srTempoLeitura = pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0, 3), index_col=0).squeeze('columns')
srTempoLazer = pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0, 4), index_col=0).squeeze('columns')
srRendimentoTeste =pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0, 5), index_col=0).squeeze('columns')
srCurso = pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0, 6), index_col=0).squeeze('columns')
srRegiao = pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='dados', usecols=(0, 7), index_col=0).squeeze('columns')

print('\n=================================')
print('\nAnálise de Atividades de Lazer e Leitura x coeficiente rendimento no teste')
print('\n=================================')

print('\n==============================================')
print('\nQuestão 1 - Conhecendo os dados (2.1 pontos)') 
print('\n==============================================')
#======================================================================
# 1- Conhecendo as Series:
# Exiba:  
# (0.3) a- JUNTO, o tempo de leitura das 5 primeiras e das 5 últimas pessoas, após ordenar por valor.
# (0.3) b- Média de idade das pessoas com 1 casa decimal .
# (0.3) c- Lista de regiões únicas,  sem repetição.
# (0.3) d- Tabela de frequência dos gêneros literários.
# (0.3) e- A quantidade de valores distintos de curso.
# (0.3) f- Juntos, o menor e maior valor de tempo em outras atividades'.
# (0.3) g- Estatísticas (juntas) de tempo de estudo (média, mediana, mínimo e máximo).
#======================================================================

# 1- Conhecendo as Series:
print("\n1.a- Tempo de leitura das 5 primeiras e 5 últimas pessoas (ordenadoe juntos):")


print("\n1.b- Média de idade das pessoas")



print("\n1.c- Lista de regiões únicas:")


print("\n1.d- Tabela de frequência dos gêneros literários:")



print("\n1.e- Quantidade de valores distintos de curso:")



print("\n1.f- Menor e maior valor de tempo em outras atividades:")


print("\n1.g- Estatísticas do tempo de estudo (média, mediana, mínimo e máximo): ")



print('\n\n==============================================')
print('\nQuestão 2 - Conhecendo algumas relações dos dados (4.0 pontos)') 
print('\n==============================================')
#======================================================================
# 2- Conhecendo algumas relaões dos Dados:
# Exiba:   
# (0.4) a- Média de idade das pessoas por curso com uma casa decimal
# (0.4) b- A idade da pessoa mais jovem que lê mais de 3 horas por semana.
# (0.4) c- Percentual de pessoas que preferem o gênero 'Ficção Científica'.
# (0.4) d- Estatísticas do coeficiente de rendimento no teste por região
#          ((média, mediana, desvio_padrao)
# (0.4) e- Tempo médio de leitura por semana para pessoas na faixa etária de 20 a 30 anos.
# (0.4) f- Curso(s) das pessoas com maior coeficiente de rendimento no teste
# (0.4) g - Gráfico de barras horizontal com a soma dos tempos de leitura 
#           das pessoas, por região
# (0.8) h -  Mediana do coeficente de rendimento no teste para as pessoas 
#            com tempo de leitura semanal superior ao tempo em outras atividades.
# (0.4) i- Correlação tempo de leitura e coeficiente de rendimento no teste
#======================================================================
print('\n2.a- Média de idade das pessoas por curso')



print('\n2.b- A idade da pessoa mais jovem que lê mais de 3 horas por semana')


print('\n2.c- Percentual de pessoas que preferem o gênero Ficção Científica')

print('\n2.d- Estatísticas do coeficiente de rendimento no teste por região')


print('\n2.e- Tempo médio de leitura por semana para pessoas na faixa etária de 20 a 30 anos')


print('\n2.f- Curso(s) das pessoas com maior coeficiente de rendimento no teste')

print('\n2.g- Gráfico de barras da Soma do Tempo de Leitura por Região')

print("\n2.h- Mediana do coeficiente de rendimento no teste para pessoas com tempo de leitura maior que outras atividades")

print('\n2.i- Correlação tempo de leitura e coeficiente de rendimento no teste')

print('\n-----------------------------------')
print('\n==============================================')



print('\n-----------------------------------')
print('\n==============================================')

print('\nQuestão 3 - Resumos e Correlações (1.6 pontos)')
# 
#======================================================================
# 3- Resumos e Correlações
#   (0,5) a- Calcule e mostre em um gráfico de barrasvertical, a diferenca entre 
#             o tempo de leitura e o tempo em outras atividades das pessoas 
#             do curso Ensino Fundamental.
#   (0,5) b- Tabela de frequência cruzada entre gênero literário e região.
#   (0,6) d- Coeficiente de rendimento no teste mediano por gênero literário/Curso.
#======================================================================
print('\n3.a- Grafico de barras da diferenca entre os tempos')


print('\n3.b- Tabela de frequência cruzada entre gênero literário e região')

print('\n3.d- Média do coeficiente de rendimento em testes por gênero literário/Curso')


print('\n-----------------------------------')
print('\n==============================================')

print('\nQuestão 4 - Categorias e Agrupamentos (2.3 pontos)')
# 


#======================================================================
# 4- Categorias e Cruzamentos:
#    (0.5) a- Crie 3 faixas de idade de mesma amplitude (Jovem, Adulto, Sênior)
#          e mostre a frequência de cada faixa.
#    (0.5) b- Crie as seguintes categorias de coeficiente de rendimento:
#           Baixo: 0 a 4.9
#           Moderado: 5.0 a 6.9
#           Alto: 7. 0 a 8.9
#           Excelente: 9.0 a 10.
#          Mostre em um gráfico de pizza a tabela de frequência percentual das categorias
#          de coeficiente de rendimento
#  
#    (0.7) c- Tabela de frequencia dos gêneros literários por curso e faixa etaria'
#    (0.7) d- Exiba o tempo médio de leitura  por faixa etária x categoria de coeficiente de rendimento.

#======================================================================
# Criando faixas etárias

print('\n4.a- Frequência de cada faixa etária:')

print('\n4.b-Tabela de frequência percentual das categorias de coeficiente de rendimento:')



print('\n\n4.c- Tabela de frequencia dos gêneros literários por curso e faixa etaria')


print('\n\n4.d- Tempo médio de leitura por faixa etária e categorias de rendimento')

print('\n\n4.d- Tempo médio de leitura por faixa etária e categorias de rendimento')



print('\n-----------------------------------')
print('\n==============================================')


#======================================================================
# 5- VAlores Ausentes
#
#    (0.5) a- Crie uma nova Series (srAus_zero)com os valores ausentes de sAus preenchidos com o valor 0
#    (0.5) a- Crie uma nova Series (srAus_med) com os valores ausentes de sAus preenchidos com o valor médio
#    (0.5) a- Crie uma nova Series (srAus_medCur)com os valores ausentes de sAus preenchidos com o valor médio por curso
#    (0.5) a- Crie uma nova Series ((srAus_medGen) com os valores ausentes de sAus preenchidos com o valor médio por gênero literário
#     Mostre,juntos, o tempo mediano e o desvio padrão da Series original (srRendimentoTeste), da Series com valores ausentes (srAus) 
#      e das preenchidas

#======================================================================


srAus=pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='ausente', usecols=(0, 1), index_col=0).squeeze('columns')



print("Comparação de métodos de preenchimento de valores ausentes")
