# -*- coding: utf-8 -*-
"""ListaExercicio3_resolvido.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ogQn0KXvQz-voJPtJkyhW25v5Sk_kXS7

## Regras gerais:

    - A resolução deve ser realizada individualmente
    - Pode realizar buscas na internet (Google) ou consultar os arquivos das aulas anteriores, mas não deve trocar informações com os demais colegas

## Avaliação de alternativas de projetos

Os dados do arquivo `projetos.csv` se referem aos valores futuros previstos para receita mensal de 5 projetos diferentes. A análise dos dados permitirá a decisão sobre o investitmento em um ou mais alternativas de projetos. Neste cenário, os dados futuros se referem ao período de 2025 e 2026.

1) Nesta etapa, faça o carregamento dos dados e apresente a df completa. (Peso: 1,0)
"""

import streamlit as st

st.set_page_config(
    page_title="Lista de Exercícios 3",
    page_icon="👋",
)

st.header("Lista de Exercícios 3")

import pandas as pd

arquivo = "projetos.csv"
df = pd.read_csv(arquivo, sep=';')
st.dataframe(df.head(len(df)))

"""2) Atualize a DataFrame criado no Exe1, adicionando mais uma linha ao final com os dados referentes ao mês de dezembro de 2026. Depois apresente as últimas linhas da df para checar se ocorreu como deveria. (Peso: 2,0)

mes | ano | Projeto1 | Projeto2 | Projeto3 | Projeto4 | Projeto5
--- | --- | -------- | -------- | -------- | -------- | --------
12 | 2026 | 29376 | 40392 | 63648 | 29376 | 25704


Dica: o método `append` parou de funcionar como alternativa para incluir dados ao final do DataFrame. Sugiro utilizar o método `concat`

obs: a partir deste ponto, utilize a df atualizada, agora com 24 meses de dados
"""

df1 = pd.DataFrame({'mes': [12], 'ano': [2026], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.dataframe(df.head(len(df)))

"""3) Apresente a soma dos valores de cada projeto agrupado por ano. (Peso: 1,0)"""

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.dataframe(df.groupby('ano')[colunas].sum())

"""4) Deseja-se calcular o Valor Presente (VP) de cada projeto, considerando uma taxa de juros mensal constante de 2%. Para isto, crie uma função `valor_presente(fluxos, taxa)` e depois aplique a função para calcular o VP de todos os projetos. (Peso: 2,0)

Dicas:
- A função `valor_presente` deve receber uma variável que contém lista/série e valor da taxa (formato número, exemplo 0.02)
- Dentro da função, deve percorrer a lista e calcular o valor presente de cada valor: VP = `valor - (valor * (taxa**t))`
- Ao final da repetição deve retornar com a soma dos VP de cada mês
- Utilize a função para calcular e apresentar o VP de cada projeto, utilizando taxa de juros de 2% para calcular. Deve apresentar os VP em formato R$ e com duas casas decimais
"""

def valor_presente(fluxos, taxa):
    total = 0
    for t, valor in enumerate(fluxos):
      VP = valor / ((1 + taxa) ** (t + 1))
      total = total + VP
    return total

st.write("Valor Presente dos projetos:")
st.write(f"Projeto1: R$ {valor_presente(df['Projeto1'], 0.02):,.2f}")
st.write(f"Projeto2: R$ {valor_presente(df['Projeto2'], 0.02):,.2f}")
st.write(f"Projeto3: R$ {valor_presente(df['Projeto3'], 0.02):,.2f}")
st.write(f"Projeto4: R$ {valor_presente(df['Projeto4'], 0.02):,.2f}")
st.write(f"Projeto5: R$ {valor_presente(df['Projeto5'], 0.02):,.2f}")

def valor_presente(fluxos, taxa):
    total = 0
    for t, valor in enumerate(fluxos):
      VP = valor - (valor * (taxa**t))
      total = total + VP
    return total

st.write("Valor Presente dos projetos:")
st.write(f"Projeto1: R$ {valor_presente(df['Projeto1'], 0.02):,.2f}")
st.write(f"Projeto2: R$ {valor_presente(df['Projeto2'], 0.02):,.2f}")
st.write(f"Projeto3: R$ {valor_presente(df['Projeto3'], 0.02):,.2f}")
st.write(f"Projeto4: R$ {valor_presente(df['Projeto4'], 0.02):,.2f}")
st.write(f"Projeto5: R$ {valor_presente(df['Projeto5'], 0.02):,.2f}")

"""5) Gere um gráfico de dispersão cruzando os dados do `Projeto1` e `Projeto2`, com marcadores verdes e em formato de estrela. (Peso: 2,0)"""

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

"""6) Crie um gráfico de linha que mostre a evolução dos valores dos projetos ao longo do tempo. (Peso: 2,0)

Dicas:
- Antes de plotar, deve criar uma nova variável `Data` que surgirá da concatenação de `ano` e `mês`. Para isto pode utilizar a função to_datetime: `pd.to_datetime(dict(year=df["ano"], month=df["mes"], day=1))`
- Depois, ordene a df utilizando a nova variável `Data`, utilizando `sort_values()`
- Para conseguir apresentar mais de uma variável (todos os projetos) no mesmo gráfico, uma dica importante está no funcionamento do pacote `matplotlib`
  - A lógica de plotar gráfico no `matplotlib` segue o caminho das funções figure (inicia ação), plot (monta o gráfico) e show (apresenta). Logo, todos os plot que forem montados entre o figure e o show vão aparecer no mesmo gráfico
  - `plt.figure(figsize=(10,6))`
  - `plt.plot()`
  - `plt.show()`
"""

df["Data"] = pd.to_datetime(dict(year=df["ano"], month=df["mes"], day=1))

df = df.sort_values("Data")
st.dataframe(df)

projetos = ["Projeto1", "Projeto2", "Projeto3", "Projeto4", "Projeto5"]

fig, ax = plt.subplots(figsize=(10,6))
for projeto in projetos:
    ax.plot(df["Data"], df[projeto], marker="o", label=projeto)

ax.set_title("Evolução dos Fluxos de Caixa dos Projetos")
ax.set_xlabel("Tempo (Ano-Mês)")
ax.set_ylabel("Valor (R$)")
ax.legend(title="Projetos")
ax.grid(True)
fig.tight_layout()
st.pyplot(fig)
