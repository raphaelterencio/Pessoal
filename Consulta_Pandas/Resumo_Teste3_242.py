"""Resumo das operações realizadas em Teste3_242.py

Este arquivo resume cada etapa da prova, com explicação e exemplo de código.
As Series envolvidas:
- srGeneroLiterario: gêneros literários
- srIdade: idade dos participantes
- srTempoLeitura: horas de leitura por semana
- srTempoLazer: horas em outras atividades por semana
- srRendimentoTeste: coeficiente de rendimento no teste
- srCurso: curso dos participantes
- srRegiao: região dos participantes
- srAus: valores ausentes de uma série

1. Carregamento das Series
# Utiliza pd.read_excel e squeeze para converter colunas em Series.
srGeneroLiterario = pd.read_excel(
    'dados_lazer_ajustado.xlsx', sheet_name='dados',
    usecols=(0,1), index_col=0
).squeeze('columns')

2. Exploração inicial dos dados
a) Concatenar primeiros e últimos valores após ordenar:
tempo_ord = srTempoLeitura.sort_values()
pd.concat([tempo_ord.head(5), tempo_ord.tail(5)])

b) Média com uma casa decimal:
f"{srIdade.mean():.1f}"

c) Valores únicos:
srRegiao.unique()

d) Frequência de gêneros:
srGeneroLiterario.value_counts()

e) Distintos em cursos:
srCurso.nunique()

f) Menor e maior valor:
srTempoLazer.agg(['min','max'])

g) Estatísticas resumidas:
srTempoLeitura.agg(['mean','median','min','max'])

3. Relações entre variáveis
a) Média de idade por curso:
srIdade.groupby(srCurso).mean().apply('{:.1f}'.format)

b) Idade mínima para leitura > 3h:
srIdade.loc[srTempoLeitura > 3].min()

c) Percentual de um gênero:
freq = srGeneroLiterario.value_counts()
f"{freq['Ficção Científica']/freq.sum()*100:.2f}%"

d) Estatísticas de rendimento por região:
srRendimentoTeste.groupby(srRegiao).agg(['mean','median','std'])

e) Média de leitura para idade 20-30:
srTempoLeitura[(srIdade >= 20)&(srIdade <= 30)].mean()

f) Cursos de maior rendimento:
srCurso.loc[srRendimentoTeste == srRendimentoTeste.max()].unique()

g) Gráfico horizontal da soma de leitura por região:
srTempoLeitura.groupby(srRegiao).sum().plot.barh()

h) Mediana de rendimento para leitura > lazer:
srRendimentoTeste.loc[srTempoLeitura > srTempoLazer].median()

i) Correlação leitura x rendimento:
srTempoLeitura.corr(srRendimentoTeste)

4. Resumos e correlações
a) Gráfico de barras da diferença leitura - lazer:
d = (srTempoLeitura - srTempoLazer).loc[srCurso=='Ensino Fundamental']
d.plot(kind='bar')

b) Tabela cruzada gênero x região:
pd.crosstab(srGeneroLiterario, srRegiao)

d) Mediana rendimento por gênero/curso:
pd.crosstab(srGeneroLiterario, srCurso, values=srRendimentoTeste, aggfunc='median')

5. Categorias e agrupamentos
a) Faixas de idade em 3 bins:
srFaixa = pd.cut(srIdade, bins=3, labels=['Jovem','Adulto','Sênior'])
srFaixa.value_counts()

b) Categorias de rendimento e gráfico de pizza:
cats = pd.cut(srRendimentoTeste, bins=[0,4.9,6.9,8.9,10],
              labels=['Baixo','Moderado','Alto','Excelente'], include_lowest=True)
cats.value_counts().plot.pie(autopct='%1.1f%%')

c) Frequência de gênero por curso e faixa etária:
srGeneroLiterario.groupby([srCurso, srFaixa]).value_counts()

d) Tempo médio leitura por faixa x categoria:
srTempoLeitura.groupby([srFaixa, cats]).mean()
pd.crosstab(srFaixa, cats, values=srTempoLeitura, aggfunc='mean')

6. Tratamento de valores ausentes
a) Preencher com zero:
srAus_zero = srAus.fillna(0)

b) Preencher com média geral:
srAus_med = srAus.fillna(srAus.mean())

c) Preencher com média por curso:
srAus_medCur = srAus.groupby(srCurso).apply(lambda g: g.fillna(g.mean()))

d) Preencher com média por gênero:
srAus_medGen = srAus.groupby(srGeneroLiterario).apply(lambda g: g.fillna(g.mean()))

e) Comparar estatísticas:
dfComp = pd.DataFrame({
    'Original': srRendimentoTeste.agg(['mean','median','std']),
    'Ausente': srAus.agg(['mean','median','std']),
    'Zero': srAus_zero.agg(['mean','median','std']),
    'Média': srAus_med.agg(['mean','median','std']),
    'Por Curso': srAus_medCur.agg(['mean','median','std']),
    'Por Gênero': srAus_medGen.agg(['mean','median','std']),
})
print(dfComp)
"""