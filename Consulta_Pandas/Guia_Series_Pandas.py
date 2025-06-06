"""Guia Completo de Operações em Series no Pandas

Este arquivo contém comandos e exemplos para consulta rápida em uma Series chamada `srValor`
e Series auxiliar `srDest`, focado em operações comuns em provas.

1. Pegar tamanho
----------------
```python
print(srValor.size)  # retorna o número total de elementos na Series
```

2. Pegar primeiros elementos / primeiro elemento
-----------------------------------------------
```python
print(srValor.head(5))  # retorna os primeiros 5 valores
print(srValor.iloc[0])  # retorna o primeiro valor
```

3. Pegar últimos elementos / último elemento
--------------------------------------------
```python
print(srValor.tail(5))   # retorna os últimos 5 valores
print(srValor.iloc[-1])  # retorna o último valor
```

4. Quantos válidos / quantos nulos
----------------------------------
```python
print(srValor.count())        # conta valores não nulos (descarta NaN)
print(srValor.isnull().sum()) # conta valores nulos (NaN)
```

5. Ordenar por índice (rótulo)
-------------------------------
```python
print(srValor.sort_index())      # retorna nova Series ordenada pelos índices
srValor.sort_index(inplace=True) # ordena no próprio objeto
```

6. Ordenar por valor (crescente e decrescente)
----------------------------------------------
```python
print(srValor.sort_values(ascending=True))   # ordem crescente
print(srValor.sort_values(ascending=False))  # ordem decrescente
```

7. Acessar apenas valores e índices
-----------------------------------
```python
print(srValor.values)  # array NumPy com apenas os valores
print(srValor.index)   # Index com apenas os rótulos
```

8. Descartar valores inválidos (NaN)
------------------------------------
```python
print(srValor.dropna())       # retorna cópia sem NaN
srValor.dropna(inplace=True)  # remove NaN na própria Series
```

9. Copiar Series
----------------
```python
copia = srValor.copy()  # cria cópia independente da Series
```

10. Selecionar elemento específico
----------------------------------
```python
print(srValor.iloc[3])            # acesso por posição
print(srValor.loc['MOTOBOY'])     # acesso por rótulo (exemplo)
```

11. Consertar valores
---------------------
# Substituição direta
```python
srValor.loc[srValor < 0] = 0
```
# Usando map
```python
mapeio = {'Velho': 'Novo'}
srDest = srDest.map(mapeio)
```
# Usando replace
```python
srDest = srDest.replace({'Velho': 'Novo'})
```

12. Aplicar função a cada elemento (apply)
------------------------------------------
```python
print(srValor.apply(lambda x: round(x, 2)))
```

13. Estatísticas básicas
------------------------
```python
total = srValor.sum()
print(total)

maior = srValor.max()
print(maior)

# Métodos de entrega com maior valor (se houver empate)
max_val = srValor.max()
metodos = srValor[srValor == max_val].index.tolist()
print(metodos)

media = srValor.mean()
print(media)

media_moto = srValor[srDest == 'MOTOBOY'].mean()
print(media_moto)

moda = srValor.mode()[0]
print(moda)
```

14. Tabela de frequência
------------------------
```python
freq = srValor.value_counts()
print(freq)
```

15. Gráficos de frequência
--------------------------
```python
import matplotlib.pyplot as plt

# Gráfico de barras
freq.plot(kind='bar')
plt.show()

# Gráfico de pizza
freq.plot(kind='pie', autopct='%1.1f%%')
plt.show()
```
"""