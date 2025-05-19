## Guia Completo de Operações em `Series` no Pandas

Este documento apresenta **comando** e **explicação** para cada uma das operações solicitadas. Para cada tópico, há exemplos práticos usando a `Series` chamada `srValor`.

---

### 1. Pegar tamanho da Series

```python
srValor.size
```

**O que faz:** Retorna o número total de elementos na Series.

---

### 2. Pegar os primeiros elementos / primeiro elemento

* **Primeiros N**

```python
srValor.head(n)
```

Retorna os primeiros `n` elementos.

* **Primeiro elemento**

```python
srValor.iloc[0]
```

Retorna o primeiro valor.

---

### 3. Pegar os últimos elementos / último elemento

* **Últimos N**

```python
srValor.tail(n)
```

Retorna os últimos `n` elementos.

* **Último elemento**

```python
srValor.iloc[-1]
```

Retorna o último valor.

---

### 4. Quantos válidos / quantos não possuem None (nulos)

* **Contar valores não nulos**

```python
srValor.count()
```

Retorna o número de elementos não `NaN`.

* **Contar valores nulos**

```python
srValor.isnull().sum()
```

Retorna o número de elementos `NaN`.

---

### 5. Exibir ordenada por índice (sem alterar original)

```python
srValor.sort_index()
```

Retorna uma nova Series ordenada pelos rótulos do índice.

---

### 6. Chamar uma função em cada elemento da Series

```python
# Exemplo: arredonda cada valor para 2 casas decimais
srValor.apply(lambda x: round(x, 2))
```

Aplica a função em cada elemento e retorna nova Series.

---

### 7. Exibir a Series ordenada por índice (in-place)

```python
srValor.sort_index(inplace=True)
```

Ordena pelos rótulos do índice modificando a Series original.

---

### 8. Exibir a Series ordenada decrescentemente por valor

```python
srValor.sort_values(ascending=False)
```

Retorna nova Series ordenada dos maiores para os menores valores.

---

## Métodos básicos de ordenação e limpeza

| Comando                               | Explicação                                                    |
| ------------------------------------- | ------------------------------------------------------------- |
| `srValor.sort_values(ascending=True)` | Ordena pelos valores em ordem crescente. Retorna nova Series. |
| `srValor.values`                      | Retorna um array NumPy com **apenas** os valores da Series.   |
| `srValor.index`                       | Retorna o objeto Index com **apenas** os rótulos da Series.   |
| `srValor.dropna()`                    | Retorna cópia sem elementos nulos (`NaN`).                    |
| `srValor.dropna(inplace=True)`        | Remove `NaN` na própria Series, sem criar cópia.              |
| `srValor.sort_index()`                | Ordena pelos rótulos do índice e retorna nova Series.         |
| `srValor.sort_index(inplace=True)`    | Ordena pelos rótulos do índice na própria Series.             |
| `srValor.sort_values(ascending=True)` | Ordena pelos valores em ordem crescente.                      |

---

## Operações de descarte, correção, cópia e seleção

* **Descarte de valores inválidos**

  ```python
  # remover NaN sem alterar original
  limpa = srValor.dropna()
  ```
* **Consertar valores**

  ```python
  # substituir todos os valores negativos por zero
  srValor = srValor.apply(lambda x: x if x >= 0 else 0)
  ```
* **Cópia da Series**

  ```python
  copia = srValor.copy()
  ```
* **Selecionar elemento específico**

  ```python
  # por posição
  valor = srValor.iloc[3]
  # por índice
  valor = srValor.loc['CHAVE']
  ```

---

## Estatísticas básicas e exemplos de uso

* **Soma de todos os valores**

  ```python
  total = srValor.sum()
  ```

* **Maior valor de entrega**

  ```python
  maior = srValor.max()
  ```

* **Índice do maior valor (meio de entrega)**

  ```python
  metodo_maior = srValor.idxmax()
  ```

* **Valor médio das entregas**

  ```python
  media = srValor.mean()
  ```

* **Valor médio das entregas via MOTOBOY**

  ```python
  media_moto = srValor.loc[srDest=='MOTOBOY'].mean()
  ```

* **Valor mais frequente (moda)**

  ```python
  moda = srValor.mode()[0]
  ```

---

## Frequência e visualizações

### Tabela de frequência (value\_counts)

```python
freq = srValor.value_counts()
print(freq)
```

Retorna Series com contagem de cada valor.

### Gráfico de barras da frequência

```python
freq.plot(kind='bar')
```

Exibe gráfico de barras vertical.

### Gráfico de pizza da frequência

```python
freq.plot(kind='pie', autopct='%1.1f%%')
```

Exibe gráfico de pizza com percentuais.

---

**Fim do Guia** — Estes comandos cobrem todas as operações práticas solicitadas, com exemplos claros do que fazem. Você pode rodar cada bloco no seu ambiente para testar diretamente.
