
# Resumo do Projeto: Agente Autônomo de Recomendação de Investimento

## Objetivo
Desenvolver um agente autônomo que automatize recomendações de investimento no mercado de ações brasileiro, utilizando aprendizado de máquina para analisar padrões de mercado e ajustar suas estratégias conforme aprende com dados históricos.

## Componentes do MVP

1. **Coleta de Dados**
   - Usar a API do Yahoo Finance com a biblioteca `yfinance` para coletar dados históricos de ações brasileiras (tickers no formato `ticker.SA`).
   - Exemplos de tickers:
     - Petrobras (PETR3): `PETR3.SA`
     - Itaú Unibanco (ITUB4): `ITUB4.SA`
     - Ambev (ABEV3): `ABEV3.SA`

2. **Pré-processamento dos Dados**
   - Limpeza e organização dos dados coletados.
   - Cálculo de indicadores técnicos relevantes (ex.: médias móveis, Índice de Força Relativa - RSI, bandas de Bollinger).

3. **Modelo de Previsão Simples**
   - Implementar um modelo como XGBoost ou um LSTM leve para prever tendências de preço com base em dados históricos.
   - Avaliação da precisão do modelo usando dados de teste.

4. **Agente de Tomada de Decisão**
   - Implementar um agente de Deep Q-Learning (DQN) simples para decidir quando comprar ou vender ações.
   - Criar um ambiente de simulação para testar as decisões do agente.

5. **Interface Simples**
   - Criar uma interface básica para exibir as recomendações do agente e as previsões do modelo.
   - A interface pode ser em linha de comando ou uma aplicação web simples.

## Considerações
- O projeto será desenvolvido em Python.
- O foco será na implementação de um MVP que contemple as funcionalidades essenciais, permitindo iterações rápidas.
- A equipe de desenvolvimento consiste em três pessoas, com grandes restrições de horário e pouca disponibilidade.

## Observações
- Manter uma boa documentação do código e do progresso do projeto.
- Estar atento a eventos econômicos e políticos que podem influenciar o mercado brasileiro.
