# Business Understanding (CRISP-DM)

## 1. Contexto do Negócio

Empresas do setor varejista precisam tomar diariamente decisões relacionadas ao reabastecimento de produtos, planejamento de estoque, promoções e logística. Essas decisões dependem diretamente da capacidade de prever a demanda futura com precisão.

Previsões imprecisas podem gerar dois problemas críticos: excesso de estoque, aumentando custos de armazenagem e risco de perdas, ou ruptura de estoque, ocasionando perda de vendas e redução da satisfação dos clientes.

Neste projeto será desenvolvido um pipeline completo de previsão de demanda utilizando dados históricos de vendas da competição M5 Forecasting, buscando construir um modelo capaz de apoiar decisões estratégicas relacionadas ao gerenciamento de estoque e planejamento operacional.

## 2. Problema de Negócio

Empresas do setor varejista enfrentam o desafio de prever com precisão a demanda futura de milhares de produtos distribuídos entre diferentes lojas e regiões. O comportamento das vendas sofre influência de fatores como sazonalidade, eventos especiais, promoções, preços e preferências dos consumidores, tornando a previsão de demanda uma tarefa complexa.

A ausência de previsões confiáveis pode resultar em dois problemas significativos: excesso de estoque, elevando custos de armazenagem e aumentando o risco de perdas, ou ruptura de estoque, ocasionando perda de vendas e redução da satisfação dos clientes.

Diante desse cenário, torna-se necessário desenvolver um modelo preditivo capaz de antecipar a demanda futura dos produtos, fornecendo informações que apoiem decisões relacionadas ao planejamento de estoque, reposição de mercadorias e gestão da cadeia de suprimentos.

## 3. Objetivos

### Objetivo Geral

Desenvolver um pipeline de previsão de demanda baseado em técnicas de Machine Learning capaz de prever a demanda futura de produtos em uma rede varejista, utilizando dados históricos de vendas, calendário e preços, com o objetivo de apoiar decisões relacionadas ao planejamento de estoque e à gestão da cadeia de suprimentos.

### Objetivos Específicos

- Compreender a estrutura, qualidade e relacionamento entre os conjuntos de dados disponibilizados.
- Realizar análises exploratórias para identificar padrões, tendências, sazonalidades e comportamentos de vendas.
- Desenvolver atributos (features) que representem adequadamente o comportamento temporal da demanda.
- Construir e comparar diferentes modelos de previsão de demanda.
- Avaliar o desempenho dos modelos por meio de métricas apropriadas para séries temporais.
- Selecionar o modelo com melhor desempenho considerando precisão e capacidade de generalização.
- Disponibilizar visualizações que auxiliem gestores na interpretação dos resultados e apoiem o processo de tomada de decisão.

## 4. Stakeholders

Os principais interessados nos resultados deste projeto são:

- **Gestores de Estoque:** responsáveis por definir níveis de estoque e planejar a reposição de produtos.
- **Equipe de Supply Chain:** utiliza as previsões para otimizar o abastecimento entre centros de distribuição e lojas.
- **Gestores Comerciais:** utilizam as previsões para planejar campanhas promocionais e ações estratégicas de vendas.
- **Diretoria Executiva:** acompanha indicadores relacionados à redução de custos, aumento da disponibilidade de produtos e melhoria da eficiência operacional.
- **Equipe de Ciência de Dados:** responsável pelo monitoramento, manutenção e evolução contínua do modelo preditivo.

## 5. Escopo do Projeto

Este projeto contempla o desenvolvimento de um pipeline completo de previsão de demanda utilizando dados históricos da competição M5 Forecasting.

O escopo inclui:

- Compreensão do problema de negócio.
- Análise exploratória dos dados.
- Preparação e transformação dos dados.
- Engenharia de atributos para séries temporais.
- Desenvolvimento e comparação de diferentes modelos de Machine Learning.
- Avaliação dos modelos utilizando métricas apropriadas.
- Geração de previsões de demanda.
- Construção de visualizações para apoio à tomada de decisão.

Não fazem parte do escopo deste projeto:

- Implantação do modelo em ambiente de produção.
- Atualização automática das previsões em tempo real.
- Integração com sistemas ERP ou plataformas corporativas.

## 6. Benefícios Esperados

A implementação de um modelo de previsão de demanda pode gerar diversos benefícios para a operação varejista, entre eles:

- Redução de rupturas de estoque, aumentando a disponibilidade de produtos para os clientes.
- Redução de excesso de estoque e dos custos de armazenagem.
- Melhoria no planejamento de compras e reposição de mercadorias.
- Apoio à definição de estratégias promocionais baseadas em previsões de demanda.
- Otimização da cadeia de suprimentos e da distribuição entre lojas.
- Apoio à tomada de decisão por meio de previsões mais confiáveis.

## 7. Critérios de Sucesso

O projeto será considerado bem-sucedido caso atenda aos seguintes critérios:

- Construção de um pipeline organizado e reprodutível para previsão de demanda.
- Desenvolvimento de modelos capazes de realizar previsões consistentes sobre dados históricos.
- Comparação técnica entre diferentes algoritmos de Machine Learning.
- Avaliação dos modelos utilizando métricas adequadas para séries temporais.
- Geração de visualizações que facilitem a interpretação dos resultados.
- Produção de documentação clara, organizada e de fácil compreensão.
- Produzir um projeto organizado, reprodutível e documentado, seguindo boas práticas de Ciência de Dados.

## 8. Limitações

Este projeto apresenta algumas limitações inerentes ao conjunto de dados utilizado:

- Os dados representam um cenário específico da competição M5 Forecasting e podem não refletir todas as características de outros ambientes varejistas.
- Informações como clima, concorrência, indicadores econômicos e comportamento dos consumidores não estão disponíveis na base.
- O modelo será desenvolvido utilizando dados históricos, assumindo que padrões observados no passado possam contribuir para previsões futuras.
- O projeto não contempla implantação em ambiente de produção nem atualização automática das previsões.

## 9. Próximos Passos

As próximas etapas do projeto serão:

1. Compreender detalhadamente a estrutura dos conjuntos de dados.
2. Realizar análise exploratória para identificar padrões e comportamentos relevantes.
3. Preparar os dados para modelagem.
4. Desenvolver atributos específicos para séries temporais.
5. Construir e comparar diferentes modelos de Machine Learning.
6. Avaliar os resultados utilizando métricas apropriadas.
7. Gerar previsões de demanda e construir visualizações para apoio à tomada de decisão.
8. Documentar todo o processo e consolidar os resultados finais do projeto.



