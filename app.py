import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# Configuração inicial do Streamlit
st.set_page_config(page_title="EnerWise 360 - Gestão Sustentável", layout="wide")

# Funções para geração de dados simulados
def generate_fake_data():
    setores = ["Docas", "Refrigeração", "Automação", "Iluminação"]
    consumo = np.random.randint(100, 2000, len(setores))
    desempenho = np.random.randint(60, 100, len(setores))
    temperatura = np.random.uniform(18, 30, len(setores))
    custo = consumo * 0.5  # Custo por kWh em R$
    emissoes = consumo * 0.2  # Emissões em kg CO2
    df = pd.DataFrame({
        "Setor": setores,
        "Consumo Atual (kWh)": consumo,
        "Desempenho (%)": desempenho,
        "Temperatura (°C)": temperatura,
        "Custo (R$)": custo,
        "Emissões (kg CO2)": emissoes
    })
    return df

def generate_benchmark_data():
    unidades = ["Armazém A", "Armazém B", "Armazém C"]
    consumo_medio = np.random.randint(4000, 6000, len(unidades))
    meta = consumo_medio - np.random.randint(100, 500, len(unidades))
    custo_medio = consumo_medio * 0.5
    emissoes = consumo_medio * 0.2
    df = pd.DataFrame({
        "Unidade": unidades,
        "Consumo Médio (kWh)": consumo_medio,
        "Meta (kWh)": meta,
        "Custo Médio (R$)": custo_medio,
        "Emissões (kg CO2)": emissoes
    })
    return df

def generate_projections(data):
    meses = ["Nov", "Dez", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out"]
    df = pd.DataFrame({
        "Mês": meses,
        "Projeção de Consumo (kWh)": data["Consumo Atual (kWh)"].sum() + np.cumsum(np.random.randint(200, 500, len(meses))),
        "Projeção de Custo (R$)": data["Custo (R$)"].sum() + np.cumsum(np.random.randint(100, 200, len(meses))),
        "Projeção de Emissões (kg CO2)": data["Emissões (kg CO2)"].sum() + np.cumsum(np.random.randint(50, 100, len(meses)))
    })
    return df

# Cabeçalho
st.title("EnerWise 360 - Painel Interativo de Gestão Sustentável")
st.markdown("### Monitoramento, Projeção e Benchmarking para Operações de Armazenagem")

# Divisão de KPIs
col1, col2, col3 = st.columns(3)
fake_data = generate_fake_data()

with col1:
    st.metric(label="Consumo Total Atual (kWh)", value=f"{fake_data['Consumo Atual (kWh)'].sum():,.0f}", delta="-5%")

with col2:
    st.metric(label="Custo Total Atual (R$)", value=f"{fake_data['Custo (R$)'].sum():,.2f}", delta="+3%")

with col3:
    st.metric(label="Emissões Totais (kg CO2)", value=f"{fake_data['Emissões (kg CO2)'].sum():,.0f}", delta="+2%")

# Monitoramento em Tempo Real
st.subheader("Monitoramento em Tempo Real")
st.dataframe(fake_data)

# Gráficos de Consumo e Custo por Setor
fig1 = px.bar(
    fake_data,
    x="Setor",
    y=["Consumo Atual (kWh)", "Custo (R$)", "Emissões (kg CO2)"],
    barmode="group",
    title="Consumo, Custo e Emissões por Setor",
    labels={"value": "Quantidade", "variable": "Indicador"}
)
st.plotly_chart(fig1, use_container_width=True)

# Projeções Futuras
st.subheader("Projeções Futuras")
projections = generate_projections(fake_data)
st.dataframe(projections)

fig2 = px.line(
    projections,
    x="Mês",
    y=["Projeção de Consumo (kWh)", "Projeção de Custo (R$)", "Projeção de Emissões (kg CO2)"],
    markers=True,
    title="Projeção de Consumo, Custo e Emissões Mensais",
    labels={"value": "Quantidade", "variable": "Indicador"}
)
st.plotly_chart(fig2, use_container_width=True)

# Benchmarking entre Unidades
st.subheader("Benchmarking entre Unidades")
benchmark_data = generate_benchmark_data()
st.dataframe(benchmark_data)

# Gráfico Interativo de Benchmarking
fig3 = px.bar(
    benchmark_data,
    x="Unidade",
    y=["Consumo Médio (kWh)", "Meta (kWh)", "Custo Médio (R$)", "Emissões (kg CO2)"],
    barmode="group",
    title="Benchmarking de Consumo, Meta, Custo e Emissões por Unidade",
    labels={"value": "Quantidade", "variable": "Indicador"}
)
st.plotly_chart(fig3, use_container_width=True)

# Conclusão
st.markdown("### Conclusão")
st.markdown("""
O painel **EnerWise 360** oferece uma visão integrada do desempenho energético atual, 
projeções futuras e benchmarking entre unidades. Ele é ideal para reduzir custos, 
promover sustentabilidade e tomar decisões baseadas em dados.
""")
