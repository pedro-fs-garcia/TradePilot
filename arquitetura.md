
# Arquitetura do Projeto: Agente Autônomo de Recomendação de Investimento
```
+---------------------+
|      Usuário        |
|  (Interface Gráfica)|
|        ou Bot       |
|    (Telegram Bot)   |
+---------------------+
          |
          v
+---------------------+
|  Agente de Invest.  | <--- Estratégia de Decisão
+---------------------+
          |
          v
+---------------------+
|   Modelo de ML      | <--- Dados de Ações
+---------------------+
          |
          v
+---------------------+
|   Coleta de Dados   | <--- API do Yahoo Finance
+---------------------+
          |
          v
+---------------------+
|  Pré-processamento  |
|      de Dados       |
+---------------------+
          |
          v
+---------------------+
|    Banco de Dados   |
|    (Local/Remoto)   |
+---------------------+
```


## 1. Visão Geral

Este documento descreve a arquitetura do projeto de um agente autônomo que automatiza recomendações de investimento em ações, utilizando inteligência artificial (IA) e aprendizado de máquina. O sistema coleta dados de ações, analisa padrões e ajusta suas recomendações com base nas previsões de um modelo de machine learning.

## 2. Componentes Principais

### 2.1 Usuário (Interface Gráfica ou Bot do Telegram)

- **Descrição:** O usuário interage com o sistema através de uma interface gráfica (ex.: aplicação web) ou via bot do Telegram.
- **Funcionalidades:**
  - Visualizar recomendações de investimento.
  - Consultar preços de ações em tempo real.
  - Receber alertas sobre mudanças significativas no mercado.

### 2.2 Agente de Investimento

- **Descrição:** Componente responsável por tomar decisões de compra ou venda com base nas recomendações do modelo de machine learning e interações do usuário.
- **Funcionalidades:**
  - Avaliar as recomendações do modelo de ML.
  - Implementar estratégias de investimento com base nas análises.
  - Adaptar as estratégias de acordo com as mudanças no mercado.

### 2.3 Modelo de Machine Learning
O agente emprega modelos de aprendizado de máquina para analisar dados históricos de ações e prever tendências futuras. Modelos como regressão linear, árvores de decisão, ou redes neurais podem ser utilizados para fazer previsões sobre o comportamento dos preços das ações.

- **Descrição:** Modelo que prevê tendências de preço com base em dados históricos e indicadores técnicos.
- **Algoritmos Sugeridos:**
  - Regressão Linear.
  - Árvores de Decisão.
  - Redes Neurais.
- **Funcionalidades:**
  - Analisar dados de ações e prever tendências futuras.
  - Aprender continuamente com novos dados para melhorar as previsões.

**Como a IA é utilizada:**
- A IA permite que o agente identifique padrões nos dados financeiros, como tendências de alta ou baixa, e reações a eventos de mercado, ajudando a informar suas recomendações de investimento.

- O agente pode ser programado para ajustar suas estratégias de investimento com base no desempenho passado e nas previsões do modelo. Isso significa que ele aprende continuamente com novos dados e melhora suas recomendações ao longo do tempo.

- A IA pode ser usada no pré-processamento de dados para extrair características relevantes, calcular indicadores técnicos e normalizar informações, aumentando a eficácia das previsões.


### 2.4 Coleta de Dados

- **Descrição:** Este componente coleta dados de ações utilizando a API do Yahoo Finance (`yfinance`).
- **Funcionalidades:**
  - Coletar dados históricos de preços de ações brasileiras.
  - Atualizar os dados periodicamente para refletir as condições do mercado em tempo real.

### 2.5 Pré-processamento de Dados

- **Descrição:** Limpa, organiza e calcula indicadores técnicos nos dados coletados antes de serem usados pelo modelo.
- **Funcionalidades:**
  - Normalizar dados.
  - Calcular indicadores técnicos (ex.: médias móveis, RSI).
  - Preparar os dados para análise pelo modelo de machine learning.

### 2.6 Banco de Dados

- **Descrição:** Armazena dados históricos e resultados para análises futuras. Pode ser uma solução local (SQLite) ou remota (MySQL).
- **Funcionalidades:**
  - Armazenar dados de ações coletados.
  - Manter um registro de recomendações e decisões do agente.
  - Permitir consultas e análises de dados históricos.

## 3. Fluxo de Dados

1. O sistema coleta dados de ações usando a API do Yahoo Finance.
2. Os dados são pré-processados para calcular indicadores e normalizar informações.
3. O modelo de machine learning utiliza esses dados para prever tendências.
4. O agente de investimento usa as previsões do modelo para tomar decisões de investimento.
5. O usuário interage com a interface ou bot para visualizar recomendações e resultados.

## 4. Interação com o Bot do Telegram

- **Comandos do Bot:**
  - `/start`: Iniciar a interação com o bot.
  - `/preco <ticker>`: Consultar o preço atual da ação especificada.
  - `/recomendacao`: Receber a recomendação de investimento mais recente.

## 5. Considerações Finais

A arquitetura proposta fornece uma visão clara de como o sistema funcionará, integrando inteligência artificial para criar um agente autônomo de recomendação de investimento. O projeto se concentrará em prever tendências no mercado de ações brasileiro e fornecer recomendações úteis para os usuários.


