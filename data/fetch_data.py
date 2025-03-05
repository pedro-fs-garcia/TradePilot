import yfinance as yf
import os

def fetch_stock_data(ticker, start_date, end_date, save_csv=True):
    """
    Coleta dados históricos de uma ação usando a API do Yahoo Finance.
    
    :param ticker: Código da ação (ex: 'PETR4.SA')
    :param start_date: Data inicial no formato 'YYYY-MM-DD'
    :param end_date: Data final no formato 'YYYY-MM-DD'
    :param save_csv: Se True, salva os dados em um arquivo CSV
    :return: DataFrame com os dados da ação
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        
        if data.empty:
            print(f"⚠️ Nenhum dado encontrado para {ticker} no período especificado.")
            return None
        
        # Salvando CSV se necessário
        if save_csv:
            os.makedirs("data/raw", exist_ok=True)
            file_path = f"data/raw/{ticker}.csv"
            data.to_csv(file_path)
            print(f"✅ Dados de {ticker} salvos em {file_path}")
        
        return data
    
    except Exception as e:
        print(f"❌ Erro ao buscar dados para {ticker}: {e}")
        return None

# Exemplo de uso
# data = fetch_stock_data('PETR4.SA', '2023-01-01', '2024-01-01')
