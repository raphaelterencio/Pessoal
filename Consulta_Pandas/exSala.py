# -*- coding: utf-8 -*-
"""
Exercicio de Series: alunos e cursos
Solução Daniel 
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
CRIAR as Series sAlCur, sAlBloco, sAlCr
'''
lIndAl=['ANNA SA','BETO SA','BUBA SI','CADU SI','DEDE SO','DINA SO','NANA Su','ZAZA SU','ZIZO SE']
lCurAl=['ENG', None, 'Engenharia','ENGENHARIA DE COMPUTACAO', 'ENGENHARIA DE COMPUTACAO', 'CIENCIA DA COMPUTACAO',
 None,'CIENCIA DOS COMPUTADORES','ENGeNHARIA']
lFaltasAl= [None, 2,None,4,2,None,6,1,10]

##################################
lCursos=['ENGENHARIA ELÉTRICA', 'ENGENHARIA QUIMICA', 'ENGENHARIA DE PRODUCAO',
 'ENGENHARIA MECANICA', 'ENGENHARIA DE COMPUTACAO', 'CIENCIA DA COMPUTACAO',
 'ENGENHARIA AMBIENTAL','ENGENHARIA']
lBlocos=['Bl6', 'Bl4', 'Bl8', 'Bl4', 'Bl8', 'Bl6', 'Bl6', 'Bl8']

###############################################################################

sAlCur=pd.Series(lCurAl,index=lIndAl)
sAlFaltas=pd.Series(lFaltasAl,index=lIndAl)
sCurBl=pd.Series(lBlocos,index=lCursos)


###############################################################################
'''
EXIBIR as series criadas
'''
print('\nsA1.Alunos x Cursos:\n')
print(sAlCur)
print('\nsA2.Alunos x Faltas:\n')
print(sAlFaltas)
print('\n-----------------------------------------------------\n')

'''
EXIBIR as 4 primeiras linhas da sAlCur: usar head()
'''
print('\nA3.4 Primeiras linhas:\n')
print(sAlCur.head(4))
print('\n-----------------------------------------------------\n')


'''
EXIBIR as 3 ultimas linhas da sAlCur: usar tail()
'''
print('\nA4.3 Últimas linhas:\n')
print(sAlCur.tail(3))
print('\n-----------------------------------------------------\n')

'''
EXIBIR as 3 primeiras junto com as 3 ultimas linhas da sAlCur: usar concat()
'''
print('\nA4.3 Primeiras e 3 Últimas linhas:\n')
print(pd.concat([sAlCur.head(3),sAlCur.tail(3)]))
print('\n-----------------------------------------------------\n')

# '''
# EXIBIR os indices  da sAlCur:  index
# '''

# print('\nA5.Índices:\n')
# print(sAlCur.index)
# print('\n-----------------------------------------------------\n')

# '''
# EXIBIR os valores  da sAlCur:  values
# '''
# print('\nA6.Valores:\n')
# print(sAlCur.values)
# print('\n-----------------------------------------------------\n')


'''
EXIBIR numero de linhas da series:  size
'''
print('\nA7.Número de linhas da series:\n')
print(sAlCur.size)
print('\n-----------------------------------------------------\n')


'''
EXIBIR numero de linhas VALIDAS da series: count()
'''
print('\nA8.Número de linhas Válidas da series:\n')
print(sAlCur.count())
print('\n-----------------------------------------------------\n')

'''
EXIBIR numero de linhas COM VALORES AUSENTES da series:
'''
qtAusentes= sAlCur.size-sAlCur.count() # OU sAlCur.isnull()).sum()  
print('\nA9.Número de linhas com Valores Ausentes da series:\n')
print(qtAusentes)
print('\n-----------------------------------------------------\n')
###############################################################################

###############################################################################

'''
CONSTRUINDO a TABELA DE FREQUENCIA: usar  value_counts()
        Curso - Qt de Ocorrências do curso
   
'''
srTFCursos=sAlCur.value_counts()
print(srTFCursos)

print('\n-----------------------------------------------------\n')

'''
VISUALIZANDO como grafico de barras: plot.bar(title='CURSOS')
A series original poderia ser visualizada graficamente ??? Porque?
'''
srTFCursos.plot.bar(title='CURSOS')
plt.show()
print('\n-----------------------------------------------------\n')

'''
VISUALIZANDO como grafico pizza e percentuais:  plot.pie(title="CURSOS")
'''
srTFCursos.plot.pie(title='CURSOS',autopct='%.1f')
plt.show()
print('\n-----------------------------------------------------\n')

###############################################################################

'''
CONSERTANDO ERROS:
   
CIENCIA DE COMPUTACAO foi lancada errada em alguns
casos como CIENCIA DOS COMPUTADORES
ENG  é ENGENHARIA
Todos devem ficar em maiúsculo
'''
def cursoCerto(v):
    d={'CIENCIA DE COMPUTADORES':'CIENCIA DA COMPUTACAO',
       'CIENCIA DOS COMPUTADORES':'CIENCIA DA COMPUTACAO',
       'ENG':"ENGENHARIA"}
    if v:
        maiusc=v.upper()
        v=d.get(maiusc,maiusc)
    return v

srCorrigida=sAlCur.apply(cursoCerto)

'''
C1.EXIBIR a series srCorrigida
'''

print(srCorrigida)
print('\n-----------------------------------------------------\n')

'''
TRABALHANDO AGORA com srCorrigida:
Fazer novamente a tabela de frequencia dos cursos, exibir, e visualizar como 
grafico de barras e grafico de pizza
'''
srTFCursos=srCorrigida.value_counts()
print(srTFCursos)
srTFCursos.plot.bar(title='CURSOS')
plt.show()
srTFCursos.plot.pie(title='CURSOS',autopct='%.1f')
plt.show()
print('\n-----------------------------------------------------\n')

###############################################################################
###############################################################################
'''
CONSERTANDO OUTROS ERROS:

TODOS OS caracteres DOS NOMES devem FICAR MAIÚSCULOS
    Aplicar o método str.upper()
    
PROBLEMA p/usar o apply: nomes são valores de índices
   
1) POSSIBILIDADE DE SOLUCAO: criar uma series invertida
    --> Novo problema: tem valores ausentes
2) OUTRA POSSIBILIDADE: recriar apenas o index

'''
srCorrigida.index=srCorrigida.index.str.upper()
sAlFaltas.index=sAlFaltas.index.str.upper()

print(srCorrigida.tail(3),sAlFaltas.tail(3))


###############################################################################
###############################################################################
'''
PREENCHENDO VALORES AUSENTES:
    Curso --> 'ENGENHARIA'
    Faltas
       -->por média geral
       -->por mediana do sobrenome
       -->por mediana do curso 
'''
 #Curso --> 'ENGENHARIA'
srCorrigida.fillna('ENGENHARIA',inplace=True)
print(srCorrigida.head())

#Faltas -->por média geral
media=int(sAlFaltas.mean())
s1=sAlFaltas.fillna(media)
print(s1)

'''
AGRUPANDO por sobrenome (função para separar o sobrenome):
  
'''
def preencheVazio(sGrupo):
    print("entra",sGrupo)
    mediana=sGrupo.median()
    sGrupo.fillna(mediana,inplace=True)
    print('sai',sGrupo)
    return sGrupo

def sobrenome(valInd):
    l=valInd.split(' ')
    return l[-1]
   

gSobrenome=sAlFaltas.groupby(by=sobrenome)
s1=gSobrenome.apply(preencheVazio)
print(s1)

'''
AGRUPANDO por Curso (srCorrigida):
  
'''
gCurso=sAlFaltas.groupby(srCorrigida)
s2=gCurso.apply(preencheVazio)
print(s2)

'''
supondo uma nova Series srCursoFaltas, índices com repetição
'''
srCursoFaltas = pd.Series(sAlFaltas.values, index=srCorrigida.values)
gAux=srCursoFaltas.groupby(level=0)
sMed=gAux.median()
s3=srCursoFaltas.fillna(sMed)
print(s3)



'''
FILTROS
'''
'''
Quais alunos com faltas>=3
'''
f1=sAlFaltas>=3
print(sAlFaltas.loc[f1])
 

'''
Quais alunos com 3<=faltas<=6
'''
f2=(sAlFaltas>=3) & (sAlFaltas<=6)
print(sAlFaltas.loc[f2])

'''
Quantos alunos com 3<=faltas<=6
'''
print(f2.sum()) 

'''
Quais cursos dos alunos com 3<=faltas<=6
'''

print(srCorrigida.loc[f2])

'''
Quais alunos com faltas ausentes
'''

print(sAlFaltas.loc[sAlFaltas.isnull()])

'''
Preenchendo as faltas ausentes com 0
'''
sAlFaltas.fillna(0,inplace=True)
'''
Quais alunos com menor número de faltas
'''
f3=sAlFaltas==sAlFaltas.min()
print(list(sAlFaltas.loc[f3].index))

'''
Quais os cursos,sem repetição, dos alunos com menor número de 
faltas
'''
print(srCorrigida.loc[f3].unique())


'''
COMPLEXO
Dados dos alunos do Bl8 com mais do que 3 faltas
'''
'''
Primeiro: Como o bloco está associado ao curso, 
          construir um filtro de quais cursos estão no bl8
'''
f5=sCurBl=='Bl8'
srCursosBl8=sCurBl.loc[f5]

'''
Segundo: Selecionar os alunos dos cursos com True no filtro
         Lembre-se: O alinhamento é pelo índice
'''
f6=srCorrigida.isin(srCursosBl8.index)
srCursos=srCorrigida.loc[f6]

'''
Terceiro: Selecionar os alunos com faltas>=3
         Lembre-se: O alinhamento é pelo índice
'''
f7=(sAlFaltas.index.isin(srCursos.index)) & (sAlFaltas >=3)
print(sAlFaltas.loc[f7])



##################################################################
'''
srTFCursos - tabela de frequencia de cursos criada a partir srCorrigida
MEDIDAS INTERESSANTES POR CURSO: CUIDADO--> dados textuais
    qt de alunos por curso, 
    curso(s) com menor quantidade de alunos, 
    curso(s) com maior quantidade de alunos,

'''
print('\n-----------------------------------------------------\n')
print('\nqt de alunos por curso:\n')
print(srTFCursos.value_counts())
print('\ncurso(s) com maior quantidade de alunos:\n')
print(srTFCursos.loc[srTFCursos==srTFCursos.max()].index.values)
print('\ncurso(s) com menor quantidade de alunos:\n')
print(srTFCursos.loc[srTFCursos==srTFCursos.min()].index.values)
print('\n-----------------------------------------------------\n')

#################################################################



