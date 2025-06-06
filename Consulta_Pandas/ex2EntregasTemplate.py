# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:37:36 2019

@author: Claudia baseado em questão de profa Joisa

Trabalhando com uma series criada a partir do arquivo excel com dados 
sobre entregas feitas por uma floricultura: meio_bairro_valor_Entrega.xlsx

O arquivo possui três colunas e cabeçalho
meio de entrega, bairro de destino, valor pago pelas flores


Qual coluna se deseja como indice => index_col ??
    --> Meio de transporte , valor  
    --> Bairro, valor
    --> (Meio de Transporte, Bairro), valor
    --> Meio de Transporte, Bairro


"""

import pandas as pd
import matplotlib.pyplot as plt

'''
Criando as series a partir de uma planilha .xlsx

-->Series com indices meio de transporte e o valor da compra (relaciona o meio de entrega com o valor da compra)
-->Series com indices meio de transporte e o  destino (relaciona o meio de entrega com o bairro de destino)
'''
srValor= pd.read_excel('meio_bairro_valor_Entrega.xlsx', header=0, usecols=(0,2),index_col=0).squeeze("columns")
                      
print('\n--Series valores das entregas (varias formas de transporte) --')
print(srValor)


srDest= pd.read_excel('meio_bairro_valor_Entrega.xlsx', header=0, usecols=(0,1),index_col=0).squeeze("columns")
                      
print('\n--Series destinos das entregas (varias formas de transporte) --')
print(srDest)

'''
CONHECENDO os dados: explorando a Series srValor criada
'''
print('\n 1- Tamanho:')
print(srValor.size)
print('\n 2- 4 primeiros:')
print(srValor.head(4))
print('\n 3- 4 ultimos:')
print(srValor.tail(4))
print('\n 4- Quantos validos (ou seja, quantos sem valor NaN) => count():')
print(srValor.count())
'''
VALORES INVALIDOS: descartando
'''
# print('\n 5- Exibindo a series sem valores invalidos (sem alterar):')
# print(srValor.dropna())
# print('\n 6- Descartar da series os valores invalidos (alterando):')
# srValor.dropna(inplace=True)
# print(srValor)



'''
CONSERTANDO VALORES: Gavea --> Gávea , Lablon --> Leblon, Copa --> Copacabana
'''
def conserta(valor):
    d={'Gavea':'Gávea',
       'Lablon':'Leblon',
       'Copa':'Copacabana'}
    return d.get(valor,valor)
# srDest.replace(['Gavea','Lablon','Copa'], ['Gávea','Leblon','Copacabana'],inplace=True)
srDest=srDest.apply(conserta)
print('\n 5 - Destinos consertados')
print(srDest)

'''
ORDENACAO
'''
print('\n 7- Exibindo a series ordenada por indice (sem alterar):')
print(srValor.sort_index())
print('\n 8- Exibindo a series ordenada decrescentemente por valor (sem alterar):')
print(srValor.sort_index(inplace=True))
'''
COPIA
'''
print('\n 9- Criando e exibindo a srCopia (uma copia de srValor) => copy()')
srCopia = srValor.copy()
print(srCopia)

print('\n 10- Ordenando a copia crescentemente por valor (alterando a series)')
print(srCopia.sort_values(ascending=True))
'''
SELECIONANDO ELEMENTOS
'''
print('\n 11- Exibir valores das entregas via VEICULO PROPRIO')
print(srValor.loc["VEICULO PROPRIO"])
print('\n 12- Exibir valores das entregas via MOTOBOY ou BICICLETA')
print(srValor.loc["MOTOBOY","BICICLETA"])
print('\n 13- Exibir todos os valores das entregas desconsiderando as RETIRADAS')



'''
SOBRE AS ENTREGAS EM GERAL
'''
print('\n 14- Qual o total geral considerando-se todas as entregas?')
# #OBS: para saber o total de todas as entregas, basta fazer o somatorio de  
# # todos os valores usando .sum()

print('\n 15- Qual o maior valor de uma entrega?')


print('\n 16- Qual o meio de entrega de algum maior valor? E SE TIVESSE MAIS DE UM?')


print('\n 17- Qual o valor medio das entregas?')


print('\n 18- Qual o valor medio das entregas via MOTOBOY?')


print('\n 18- Qual o valor mais frequente? mode')



'''
APLICANDO UMA FUNÇÃO SOBRE OS VALORES
'''
print('\n 19- Exibir valores das entregas com 2 casas decimais e R$')


# Construir uma nova Series com valores líquidos, isto é 
#descontando o imposto
# Criar a srLiquido: valores até 25 reais (inclusive) pagam 0%, 
# entre 25 e 100 pagaram  pa%  e acima de 100 pagam pb%
# Utilizar uma funcao calculaImposto que, alem do valor da compra, recebe 
# pa e pb e retorna o valor líquido recebido 
#( valor da compra - imposto)
def detImposto(val,pa,pb):
    if val <= 25:
        return 0
    elif val<= 100:
        return val*(1-pa/100)
    else:
        return val*(1-pb/100)


print('\n 20- Exibir valores líquidos')

 


'''
CATEGORIZANDO: criando faixas de valores para OS VALORES DAS ENTREGAS
'''
'''
21- Crie uma nova series em que cada valor será uma dentre as 3 faixas de valores 
considerando-se simplesmente o intervalo de valores das entregas dividido por 3'
=>  pd.cut()
'''
print('\n 21- Nova series em que os valores estão divididos em 3 faixas')


'''
22 - Crie uma nova series com as seguintes categorias (faixa de valor a qual o 
valor da series original pertence: de 0 a 40(inclusive), de 40 a 100(inclusive),
de 100 a 300(inclusive), acima de 300). As categorias devem ser convenientemente 
rotuladas como BARATA, REGULAR, CARA, EXAGERADA. Nome da series srCat.
=> pd.cut com labels definidos

'''

print('\n 22- Nova series em que os valores vao de BARATA ate EXAGERADA')



'''
23 - A partir da srCat crie a tabela de frequencia de cada categoria, ou seja, 
uma series com cada categoria e o numero absoluto de ocorrencias dessa categoria 
na srCat. Nome: srTabFreqCat
=> value.counts()
==> colocar os indices na ordem correta (reindex)
'''

print('\n 23a- Tabela de Frequencia das categorias de preco ')


print('\n 23b- Tabela de Frequencia das categorias de preco (de BARATA a EXAGERADA) ')

# # Tabela de Frequencia Relativa ou Percentual
print('\n 23c- Tabela de Frequencia Relativa das categorias de preco (de BARATA a EXAGERADA) ')


print('\n 23d- Tabela de Frequencia dos destinos ')

'''
ATENCAO: SOBRE OS  MEIOS DE ENTREGA
'''
print('\n 24- Exiba uma unica vez cada meio de entrega')


print('\n 25- Quantos sao meios de entrega distintos')


'''
26 - Exibir cada meio de entrega e quantas entregas foram feitas com 
 essa forma (Tabela de Frequencia do INDICE) =>sr.index.value_counts()
'''
print('\n 27-Meios de entrega e seus numeros de ocorrencias:Tab de Freq do INDICE')

print('\n 28-Qual o meio de entrega mais utilizado?')


print('\n 29- Qual um meio de entrega com menor valor?')

'''
VISUALIZACAO
'''
print('\n 30- Grafico de barras  de srValor ')


print('\n 31- Grafico de barras de srCat')


print('\n 32- Grafico de pizza de srCat ')


print('\n 33- Grafico de barras da Tabela de Frequencia dos Meios de Entrega ')


print('\n 34- Grafico de pizza da Tabela de Frequencia dos Meios de Entrega ')


'''
Agrupamentos e Análises Cruzadas
Agrupamentos por meio de transporte e categorias de valor permitem 
identificar padrões sobre o comportamento das entregas.
'''

## Agrupando por meio de transporte  (index)
print('\n 35 - Quantidade de entregas por meio de transporte:')

gp_por_transporte =srDest.groupby(level=0)
# Analisando o total, maior e menor valor por meio de transporte
print('\n 36 - Total, Maior e menor valor por meio de transporte:\n')

# # Tabela cruzada entre meio de transporte e bairro de destino
# print('\n37 -  Tabela cruzada entre meio de transporte e bairro de destino:')

## Agrupando por destino (srDest) 
# como tem repetição de indices --> classificar ambos


print('\n 38 - Quantidade de entregas por destino:')


# # Total e média dos valores por bairro de destino
# print('\n 39 - Resumo dos valores por bairro de destino:\n')


# # Tabela cruzada entre meio de transporte e bairro de destino
# print('\n40 -  Tabela cruzada entre meio de transporte e bairro de destino:')
'''
Correlações e Referências Cruzadas
Para ir além das análises de valores, podemos estudar como o tipo de meio 
de transporte afeta o valor pago pelas flores, utilizando correlações e 
referências cruzadas.
'''
# Analise Meio de Transporte e Valor
# Resumos entre os grupos de valor e os meios de transporte

print('\n 41 - Média e Mediana de valor por categoria de preço:')

# # Análise de cruzamento entre meio de transporte e valores categorizados
print('\n 42 - Categorias de transporte x valores categorizados:')


# # Análise de cruzamento entre meio de transporte e destino
print('\n 43a -  meio de transporte x destinos: qunatidades')


print('\n 43b -  meio de transporte x destinos: valor total')


print('\n 44 - valor total por categoria preco x destinos:') # como tem repetição usar .values



'''
nsights Finais
Valor Médio e Faixas de Preço:

As entregas via MOTOBOY apresentam um valor médio elevado, o que sugere que este meio de transporte é preferido para pedidos mais caros.
Entregas por Veículo Próprio tendem a ter uma maior variação, indicando que são usadas para entregas com valores muito altos ou muito baixos.
Impostos e Valores Líquidos:

Aplicando impostos com diferentes faixas de desconto, percebemos que entregas com valores maiores pagam mais impostos, impactando o valor final recebido. Essa análise pode ser útil para determinar o custo-benefício de determinadas formas de entrega.
Categorias de Valor:

A maioria das entregas se concentra nas faixas REGULAR (R$40-R$100), indicando que os clientes preferem pagar um valor intermediário pelas entregas de flores.
Meios de Transporte e Destinos:

As entregas por MOTOBOY e VEÍCULO PRÓPRIO são as mais frequentes, sugerindo que essas opções devem continuar sendo foco para otimizar a logística da floricultura.
Promoções e Estratégias de Marketing:

Promoções para entregas com valores mais altos podem ser eficazes para incentivar o uso de meios como o MOTOBOY, que já é associado a maiores gastos.
Regiões ou bairros com menor frequência de entregas poderiam ser alvo de campanhas promocionais para aumentar a demanda.
'''