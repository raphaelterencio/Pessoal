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
tempo_leitura_ordenado = srTempoLeitura.sort_values()
print(pd.concat([tempo_leitura_ordenado.head(5), tempo_leitura_ordenado.tail(5)]))


print("\n1.b- Média de idade das pessoas")
media_idade = srIdade.mean()
print(f'{media_idade:.1f}')



print("\n1.c- Lista de regiões únicas:")
regioes_unicas = srRegiao.unique()
print(regioes_unicas)



print("\n1.d- Tabela de frequência dos gêneros literários:")
frequencia_genero = srGeneroLiterario.value_counts()
print(frequencia_genero)



print("\n1.e- Quantidade de valores distintos de curso:")
valores_distintos_curso = srCurso.nunique()
print(valores_distintos_curso)



print("\n1.f- Menor e maior valor de tempo em outras atividades:")
print(srTempoLazer.agg(['min','max']))


print("\n1.g- Estatísticas do tempo de estudo (média, mediana, mínimo e máximo): ")
estatisticas_tempo_estudo = srTempoLeitura.agg(['mean', 'median', 'min', 'max'])
print(estatisticas_tempo_estudo)


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
print(srIdade.groupby(srCurso).mean().apply('{:.1f}'.format))


print('\n2.b- A idade da pessoa mais jovem que lê mais de 3 horas por semana')
print(srIdade.loc[srTempoLeitura > 3].min())

print('\n2.c- Percentual de pessoas que preferem o gênero Ficção Científica')
ficcao_pct = frequencia_genero.loc['Ficção Científica']/frequencia_genero.sum()* 100
print(f'{ficcao_pct:.2f}%')

print('\n2.d- Estatísticas do coeficiente de rendimento no teste por região')
print(srRendimentoTeste.groupby(srRegiao).agg(['mean', 'median', 'std']))

print('\n2.e- Tempo médio de leitura por semana para pessoas na faixa etária de 20 a 30 anos')
print(srTempoLeitura[(srIdade >= 20) & (srIdade <= 30)].mean())

print('\n2.f- Curso(s) das pessoas com maior coeficiente de rendimento no teste')
print(srCurso.loc[srRendimentoTeste==srRendimentoTeste.max()].values)

print('\n2.g- Gráfico de barras da Soma do Tempo de Leitura por Região')
soma_tempo_leitura_por_regiao = srTempoLeitura.groupby(srRegiao).sum()
soma_tempo_leitura_por_regiao.plot.barh( figsize=(8, 6),title='Soma do Tempo de Leitura por Região')
plt.show()

print("\n2.h- Mediana do coeficiente de rendimento no teste para pessoas com tempo de leitura maior que outras atividades")
filtro_leitura_maior_lazer = srTempoLeitura > srTempoLazer
mediana_coef_rendimento = srRendimentoTeste.loc[filtro_leitura_maior_lazer].median()
print(f"{mediana_coef_rendimento:.2f}")

print('\n2.i- Correlação tempo de leitura e coeficiente de rendimento no teste')
correlacao = srTempoLeitura.corr(srRendimentoTeste)
print(f' {correlacao:.2f}')

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
diferenca_tempo = srTempoLeitura - srTempoLazer
diferenca_tempo=diferenca_tempo.loc[srCurso=='Ensino Fundamental']
diferenca_tempo.plot(kind='bar', color='lightgreen')
plt.title('Diferença entre Tempo de Leitura e Tempo em Outras Atividades')
plt.show()

print('\n3.b- Tabela de frequência cruzada entre gênero literário e região')
print(pd.crosstab(srGeneroLiterario, srRegiao))


print('\n3.d- Média do coeficiente de rendimento em testes por gênero literário/Curso')
print(pd.crosstab(srGeneroLiterario, srCurso, aggfunc='median', values=srRendimentoTeste))

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
srFaixaEtaria = pd.cut(srIdade, bins=3, labels=['Jovem', 'Adulto', 'Sênior'])
print(srFaixaEtaria.value_counts())

print('\n4.b-Tabela de frequência percentual das categorias de coeficiente de rendimento:')
categorias_rendimento = pd.cut(
    srRendimentoTeste, 
    bins=[0, 4.9, 6.9, 8.9, 10.0], 
    labels=['Baixo', 'Moderado', 'Alto', 'Excelente'],
    include_lowest=True
)

frequencia_rendimento = categorias_rendimento.value_counts()
plt.figure(figsize=(8, 6))
frequencia_rendimento.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribuição Percentual das Categorias de Coeficiente de Rendimento')
plt.ylabel('')  # Remove o rótulo do eixo y para o gráfico de pizza
plt.show()


print('\n\n4.c- Tabela de frequencia dos gêneros literários por curso e faixa etaria')
g4c=srGeneroLiterario.groupby([srCurso,srFaixaEtaria])
print(g4c.value_counts())


print('\n\n4.d- Tempo médio de leitura por faixa etária e categorias de rendimento')
print(srTempoLeitura.groupby([srFaixaEtaria, categorias_rendimento]).mean().apply('{:.1f}'.format))

print('\n\n4.d- Tempo médio de leitura por faixa etária e categorias de rendimento')

print(pd.crosstab(srFaixaEtaria, categorias_rendimento,aggfunc='mean',values=srTempoLeitura))


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

def mediaGrupo(grupo):
    med=grupo.mean()
    grupo.fillna(med,inplace=True)
    return grupo


srAus=pd.read_excel('dados_lazer_ajustado.xlsx', sheet_name='ausente', usecols=(0, 1), index_col=0).squeeze('columns')

srAus_zero = srAus.fillna(0)
srAus_med = srAus.fillna(srAus.mean())
grCur=srAus.groupby(srCurso)
grGen=srAus.groupby(srGeneroLiterario)

srAus_medCur=grCur.apply(mediaGrupo)
srAus_medGen=grGen.apply(mediaGrupo)

dfCompara=pd.DataFrame([srRendimentoTeste.agg(['mean','median','std']),
                        srAus.agg(['mean','median','std']),
                        srAus_zero.agg(['mean','median','std']),
                        srAus_med.agg(['mean','median','std']),
                        srAus_medCur.agg(['mean','median','std']),
                        srAus_medGen.agg(['mean','median','std'])],
                       index=['Original','Ausente','Com Zero','Com Media','Por Curso','Por Genero'],
                       
                      )

print("Comparação de métodos de preenchimento de valores ausentes")
print(dfCompara)