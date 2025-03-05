```
TradePilot/
│── data/                  # Armazena dados brutos e processados
│   ├── raw/               # Dados brutos coletados da API
│   ├── processed/         # Dados tratados e prontos para uso no modelo
│   ├── indicators.py      # Cálculo de indicadores financeiros
│   ├── fetch_data.py      # Script para coletar dados do Yahoo Finance
│── models/                # Modelos de IA para previsão e recomendação
│   ├── train.py           # Treinamento do modelo
│   ├── evaluate.py        # Avaliação de desempenho do modelo
│   ├── predictor.py       # Script para previsões do modelo treinado
│── agent/                 # Implementação do agente autônomo
│   ├── decision_maker.py  # Lógica de tomada de decisão do agente
│   ├── recommender.py     # Geração de recomendações baseadas nas previsões
│── api/                   # API para exposição dos dados e previsões
│   ├── app.py             # Servidor Flask para interagir com o agente
│   ├── routes.py          # Definição das rotas da API
│── ui/                    # Interface do usuário (CLI, bot ou web)
│   ├── cli.py             # Interface de linha de comando
│   ├── dashboard/         # Interface web (React, Flask ou outra tecnologia)
│── utils/                 # Utilitários e funções auxiliares
│   ├── config.py          # Configuração global da aplicação
│   ├── logger.py          # Sistema de logs
│── tests/                 # Testes unitários e de integração
│   ├── test_fetch_data.py # Testes para coleta de dados
│   ├── test_models.py     # Testes para os modelos de IA
│   ├── test_agent.py      # Testes para o agente autônomo
|
│── requirements.txt       # Dependências do projeto (Flask, scikit-learn, etc.)
│── README.md              # Documentação do projeto
│── .gitignore             # Arquivos ignorados pelo Git

```