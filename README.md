# 📈 Retail Demand Forecasting

Projeto de Ciência de Dados aplicado à **previsão de demanda no varejo**, desenvolvido a partir do dataset **M5 Forecasting – Accuracy**, disponibilizado pelo Walmart.

O projeto simula um cenário real de planejamento de demanda, utilizando histórico de vendas, variáveis temporais, calendário, eventos e indicadores promocionais para estimar a demanda futura de produtos.

O desenvolvimento segue uma abordagem estruturada baseada em **CRISP-DM**, passando pelo entendimento do negócio, exploração dos dados, preparação, engenharia de atributos, desenvolvimento do modelo e geração de previsões futuras.

---

## 🎯 Objetivo do Projeto

Construir um pipeline de previsão capaz de estimar a demanda diária de diferentes séries de produtos, fornecendo informações que poderiam apoiar decisões como:

- Planejamento de estoque;
- Reposição de produtos;
- Identificação de itens com maior demanda esperada;
- Planejamento operacional;
- Redução de rupturas e excesso de estoque;
- Apoio à tomada de decisão baseada em dados.

O foco não está apenas na construção do modelo, mas na criação de um **fluxo completo de previsão de demanda**, desde os dados históricos até a geração de um horizonte futuro de previsões.

---

## 🏢 Contexto de Negócio

Em operações de varejo, prever a demanda futura é importante para equilibrar disponibilidade de produtos e eficiência operacional.

Uma previsão inadequada pode resultar em:

- excesso de estoque;
- ruptura de produtos;
- aumento de custos operacionais;
- perda de vendas;
- decisões de compra menos eficientes.

Neste projeto, o problema é tratado como uma tarefa de **previsão de demanda diária**, utilizando informações históricas de vendas e variáveis que podem influenciar o comportamento da demanda.

---

## 📊 Dataset

O projeto utiliza o dataset **M5 Forecasting – Accuracy**.

Os dados originais contêm informações de vendas de produtos do Walmart, incluindo:

- histórico diário de vendas;
- produtos;
- departamentos;
- categorias;
- lojas;
- estados;
- calendário;
- eventos;
- preços.

Os arquivos originais não são versionados neste repositório devido ao seu tamanho.

Para reproduzir o projeto, os arquivos devem ser disponibilizados em:

```text
data/raw/
```

Principais arquivos utilizados:

```text
calendar.csv
sales_train_validation.csv
sell_prices.csv
```

---

## 🔎 Abordagem Analítica

O projeto foi estruturado seguindo as principais etapas do **CRISP-DM**:

### 1. Business Understanding

Definição do problema de negócio, objetivo da previsão e possíveis aplicações dos resultados.

### 2. Data Understanding

Análise da estrutura dos dados, dimensões, variáveis, distribuição das vendas, produtos, lojas, categorias e comportamento temporal.

### 3. Exploratory Data Analysis

Investigação de padrões relacionados a:

- comportamento temporal;
- dias da semana;
- meses;
- categorias;
- departamentos;
- lojas;
- estados;
- eventos;
- SNAP;
- preços;
- concentração da demanda por produtos.

### 4. Data Preparation

Preparação dos dados para modelagem, incluindo:

- transformação do formato dos dados;
- tratamento de variáveis;
- integração com calendário;
- preparação das variáveis categóricas;
- organização temporal;
- separação entre histórico e horizonte futuro.

### 5. Feature Engineering

Foram desenvolvidas variáveis capazes de representar o comportamento histórico e temporal da demanda.

Entre os principais atributos utilizados estão:

**Lags**

```text
lag_1
lag_7
lag_14
lag_28
```

**Médias móveis**

```text
rolling_mean_7
rolling_mean_14
rolling_mean_28
```

**Variáveis temporais**

```text
wday
weekday
month
year
week_of_year
day_num
```

**Eventos e calendário**

```text
event_name_1
event_type_1
event_name_2
event_type_2
```

**SNAP**

```text
snap_CA
snap_TX
snap_WI
snap
```

Também foram utilizadas informações de identificação das séries:

```text
item_id
store_id
```

---

## 🤖 Model Development

O modelo final utilizado foi o **LightGBM**, escolhido por sua capacidade de lidar com grandes volumes de dados tabulares e relações não lineares entre as variáveis.

O modelo foi ajustado utilizando dados históricos e posteriormente avaliado em um conjunto de validação temporal.

### Modelo final

```text
Algoritmo: LightGBM
Objetivo: Regressão
Best Iteration: 632
```

### Métricas de avaliação

| Métrica | Resultado |
|---|---:|
| MAE | 1.0350 |
| RMSE | 1.9974 |

O MAE representa o erro absoluto médio das previsões, enquanto o RMSE atribui maior peso a erros mais elevados.

---

## 🔮 Forecasting

Após o treinamento e avaliação do modelo, foi realizada uma previsão recursiva para os próximos **28 dias**.

### Horizonte de previsão

```text
Início: 25/04/2016
Fim:    22/05/2016
```

Foram geradas:

```text
3.049 séries
85.372 previsões
28 dias por série
```

O resultado final foi armazenado em:

```text
data/processed/forecast_28_days.parquet
```

---

## 📌 Principais Resultados

A previsão gerada permite analisar a demanda esperada ao longo do horizonte futuro.

Entre os itens com maior demanda prevista no período estão:

| Item | Demanda prevista |
|---|---:|
| FOODS_3_090 | 1.506,73 |
| FOODS_3_120 | 1.269,95 |
| FOODS_3_586 | 1.116,01 |
| FOODS_3_252 | 1.022,04 |
| FOODS_3_064 | 718,49 |

A análise também permite observar o comportamento agregado da demanda ao longo dos dias previstos, identificando padrões temporais e variações semanais.

---

## 🧠 Principais Insights

A análise exploratória e o processo de modelagem evidenciaram alguns padrões relevantes:

- A demanda apresenta comportamento temporal e variações ao longo da semana.
- Existe concentração significativa de vendas em determinados produtos.
- Categorias e departamentos apresentam diferentes níveis de demanda.
- Lojas e estados possuem comportamentos distintos.
- Eventos e variáveis de calendário podem contribuir para explicar alterações na demanda.
- As variáveis históricas, especialmente os lags e médias móveis, são fundamentais para representar a dinâmica recente das vendas.
- A combinação entre histórico de demanda e variáveis temporais permite construir um modelo capaz de gerar previsões para períodos ainda não observados.

---

## 🗂️ Estrutura do Projeto

```text
retail-demand-forecasting/
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   │
│   └── processed/
│       ├── sales_features.parquet
│       ├── train_modeling.parquet
│       ├── validation_modeling.parquet
│       └── forecast_28_days.parquet
│
├── docs/
│   └── 01_business_understanding.md
│
├── models/
│   ├── lightgbm_final.txt
│   └── lightgbm_final_metadata.json
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_data_preparation.ipynb
│   ├── 05_model_development.ipynb
│   └── 06_forecasting.ipynb
│
├── reports/
│   ├── figures/
│   └── tables/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── utils/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologias

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- Matplotlib
- Jupyter Notebook
- PyArrow
- Git
- GitHub

---

## ⚙️ Reprodução do Projeto

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd retail-demand-forecasting
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente

No Windows:

```bash
.venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Adicionar os dados

Coloque os arquivos originais do M5 Forecasting em:

```text
data/raw/
```

### 6. Executar os notebooks

A execução deve seguir a ordem:

```text
01_data_understanding.ipynb
02_exploratory_data_analysis.ipynb
03_feature_engineering.ipynb
04_data_preparation.ipynb
05_model_development.ipynb
06_forecasting.ipynb
```

---

## 📦 Artefatos do Modelo

O modelo final treinado está disponível em:

```text
models/lightgbm_final.txt
```

As informações de configuração e avaliação do modelo estão disponíveis em:

```text
models/lightgbm_final_metadata.json
```

O arquivo final de previsões está disponível em:

```text
data/processed/forecast_28_days.parquet
```

---

## 📈 Resultado Final

O projeto entrega um pipeline completo de **previsão de demanda**, contemplando:

```text
Dados históricos
      ↓
Entendimento dos dados
      ↓
Análise exploratória
      ↓
Preparação
      ↓
Feature Engineering
      ↓
Modelagem
      ↓
Avaliação
      ↓
Previsão de 28 dias
      ↓
Forecast final
```

O resultado pode servir como base para aplicações de planejamento de estoque, reposição, operações e análise de demanda no varejo.

---

## 🚀 Status

**Projeto concluído.**

O pipeline principal de previsão foi desenvolvido, avaliado e utilizado para gerar um horizonte de 28 dias de demanda futura.

---

## 👤 Autor

**Eduardo Martins**

Data Science | Automação | Dados | Desenvolvimento

[GitHub](https://github.com/eduardo-martins-tech)
