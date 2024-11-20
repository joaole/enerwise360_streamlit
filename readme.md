# **EnerWise 360 - Painel Interativo de Gestão Sustentável**

Este repositório contém o código para o **EnerWise 360**, um painel interativo desenvolvido com **Streamlit** para monitoramento, projeções e benchmarking em operações de armazenagem. O objetivo principal é facilitar a tomada de decisões sustentáveis e baseadas em dados.

---

## **Índice**
1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Como Executar](#como-executar)
5. [Estrutura do Código](#estrutura-do-código)
6. [Documentação do Código](#documentação-do-código)
7. [Contribuições](#contribuições)

---

## **Visão Geral**
O painel **EnerWise 360** fornece uma visão integrada do desempenho energético em operações de armazenagem, permitindo:
- Monitoramento em tempo real de consumo energético, custo e emissões.
- Projeção de tendências futuras.
- Benchmarking entre diferentes unidades operacionais.

---

## **Funcionalidades**
### 1. **Monitoramento em Tempo Real**
- Exibição de métricas principais:
  - Consumo total atual (kWh).
  - Custo total atual (R$).
  - Emissões totais (kg CO2).
- Tabela interativa com dados por setor (Docas, Refrigeração, Automação, Iluminação).
- Gráfico comparativo entre setores.

### 2. **Projeções Futuras**
- Cálculo de projeções mensais para consumo, custo e emissões.
- Linha temporal mostrando tendências previstas.

### 3. **Benchmarking**
- Comparação entre diferentes unidades operacionais (Armazém A, B, C).
- Gráficos interativos mostrando consumo médio, metas, custos e emissões.

---

## **Tecnologias Utilizadas**
- **Python**: Linguagem base do projeto.
- **Streamlit**: Framework para criação de interfaces interativas.
- **Pandas**: Manipulação e análise de dados.
- **NumPy**: Geração de dados simulados.
- **Plotly**: Visualização de gráficos interativos.

---

## **Como Executar**

### Pré-requisitos
1. Certifique-se de ter o Python 3.8+ instalado.
2. Instale as dependências:
   ```bash
   pip install streamlit pandas numpy plotly
   ```

### Instruções de Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/enerwise360.git
   ```
2. Navegue até o diretório:
   ```bash
   cd enerwise360
   ```
3. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

---

## **Estrutura do Código**

```plaintext
enerwise360/
├── app.py               # Código principal do painel
├── README.md            # Documentação do projeto
├── requirements.txt     # Dependências do projeto
```

---

## **Documentação do Código**

### Configuração Inicial
```python
st.set_page_config(page_title="EnerWise 360 - Gestão Sustentável", layout="wide")
```
- Configura o título e layout do painel Streamlit.

### Geração de Dados Simulados
#### 1. **Dados por Setor**
```python
def generate_fake_data():
    setores = ["Docas", "Refrigeração", "Automação", "Iluminação"]
    consumo = np.random.randint(100, 2000, len(setores))
    desempenho = np.random.randint(60, 100, len(setores))
    temperatura = np.random.uniform(18, 30, len(setores))
    custo = consumo * 0.5
    emissoes = consumo * 0.2
    return pd.DataFrame({
        "Setor": setores,
        "Consumo Atual (kWh)": consumo,
        "Desempenho (%)": desempenho,
        "Temperatura (°C)": temperatura,
        "Custo (R$)": custo,
        "Emissões (kg CO2)": emissoes
    })
```

#### 2. **Benchmarking**
```python
def generate_benchmark_data():
    unidades = ["Armazém A", "Armazém B", "Armazém C"]
    consumo_medio = np.random.randint(4000, 6000, len(unidades))
    meta = consumo_medio - np.random.randint(100, 500, len(unidades))
    custo_medio = consumo_medio * 0.5
    emissoes = consumo_medio * 0.2
    return pd.DataFrame({
        "Unidade": unidades,
        "Consumo Médio (kWh)": consumo_medio,
        "Meta (kWh)": meta,
        "Custo Médio (R$)": custo_medio,
        "Emissões (kg CO2)": emissoes
    })
```

#### 3. **Projeções Futuras**
```python
def generate_projections(data):
    meses = ["Nov", "Dez", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out"]
    return pd.DataFrame({
        "Mês": meses,
        "Projeção de Consumo (kWh)": data["Consumo Atual (kWh)"].sum() + np.cumsum(np.random.randint(200, 500, len(meses))),
        "Projeção de Custo (R$)": data["Custo (R$)"].sum() + np.cumsum(np.random.randint(100, 200, len(meses))),
        "Projeção de Emissões (kg CO2)": data["Emissões (kg CO2)"].sum() + np.cumsum(np.random.randint(50, 100, len(meses)))
    })
```

### KPIs e Gráficos
- **KPIs**:
  ```python
  st.metric(label="Consumo Total Atual (kWh)", value=f"{fake_data['Consumo Atual (kWh)'].sum():,.0f}", delta="-5%")
  ```
- **Gráficos Interativos**:
  ```python
  fig1 = px.bar(fake_data, x="Setor", y=["Consumo Atual (kWh)", "Custo (R$)", "Emissões (kg CO2)"], barmode="group")
  st.plotly_chart(fig1, use_container_width=True)
  ```

---
