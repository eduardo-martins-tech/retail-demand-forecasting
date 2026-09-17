import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# --------------------------------------------------
# Configuração da página
# --------------------------------------------------

st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Carregamento dos dados
# --------------------------------------------------

@st.cache_data
def load_forecast():
    BASE_DIR = Path(__file__).resolve().parent.parent

    df = pd.read_parquet(
        BASE_DIR / "data" / "processed" / "forecast_28_days.parquet"
    )

    return df


forecast = load_forecast()


# --------------------------------------------------
# Preparação
# --------------------------------------------------

forecast["d"] = forecast["d"].astype(str)

forecast["prediction"] = forecast["prediction"].clip(lower=0)

forecast["item_id"] = forecast["item_id"].astype(str)
forecast["store_id"] = forecast["store_id"].astype(str)


# --------------------------------------------------
# Título
# --------------------------------------------------

st.title("Retail Demand Forecasting")

st.markdown(
    """
    **Previsão de demanda para os próximos 28 dias**

    Dashboard executivo para análise da demanda prevista por série,
    produto e período.
    """
)


# --------------------------------------------------
# Filtros
# --------------------------------------------------

st.sidebar.header("Filtros")

items = sorted(forecast["item_id"].unique())

selected_item = st.sidebar.selectbox(
    "Produto",
    ["Todos"] + items
)


if selected_item != "Todos":
    filtered_forecast = forecast[
        forecast["item_id"] == selected_item
    ].copy()
else:
    filtered_forecast = forecast.copy()


# --------------------------------------------------
# KPIs
# --------------------------------------------------

total_demand = filtered_forecast["prediction"].sum()

average_daily = (
    filtered_forecast
    .groupby("d")["prediction"]
    .sum()
    .mean()
)

number_series = (
    filtered_forecast[["item_id", "store_id"]]
    .drop_duplicates()
    .shape[0]
)

forecast_days = filtered_forecast["d"].nunique()


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Demanda prevista",
    f"{total_demand:,.0f}"
)

col2.metric(
    "Média diária",
    f"{average_daily:,.0f}"
)

col3.metric(
    "Séries",
    f"{number_series:,}"
)

col4.metric(
    "Dias previstos",
    forecast_days
)


# --------------------------------------------------
# Demanda prevista por dia
# --------------------------------------------------

st.subheader("Demanda prevista por dia")

daily_forecast = (
    filtered_forecast
    .groupby("d", as_index=False)["prediction"]
    .sum()
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    daily_forecast["d"],
    daily_forecast["prediction"],
    marker="o"
)

ax.set_xlabel("Dia")
ax.set_ylabel("Demanda prevista")
ax.set_title("Evolução da demanda prevista")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)


# --------------------------------------------------
# Top 10 produtos
# --------------------------------------------------

st.subheader("Top 10 produtos por demanda prevista")

top_products = (
    filtered_forecast
    .groupby("item_id")["prediction"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.barh(
    top_products.index,
    top_products.values
)

ax.set_xlabel("Demanda prevista")
ax.set_ylabel("Produto")
ax.set_title("Top 10 produtos")

plt.tight_layout()

st.pyplot(fig)


# --------------------------------------------------
# Tabela
# --------------------------------------------------

st.subheader("Detalhamento da previsão")

display_columns = [
    "item_id",
    "store_id",
    "d",
    "prediction"
]

st.dataframe(
    filtered_forecast[display_columns]
    .sort_values(
        ["item_id", "store_id", "d"]
    ),
    use_container_width=True,
    hide_index=True
)