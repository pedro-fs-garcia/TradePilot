import pandas as pd
import os

def calculate_indicators(file_path):
    """
    Calcula indicadores financeiros básicos a partir dos dados da ação.
    
    :param file_path: Caminho do arquivo CSV contendo os dados da ação.
    :return: DataFrame com os indicadores adicionados.
    """
    if not os.path.exists(file_path):
        print(f"❌ Arquivo {file_path} não encontrado.")
        return None
    
    try:
        df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
        
        # Média Móvel Simples (SMA) de 20 dias
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        
        # Média Móvel Exponencial (EMA) de 20 dias
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
        
        # Índice de Força Relativa (RSI) - 14 períodos
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI_14'] = 100 - (100 / (1 + rs))
        
        # Salvando os dados processados
        processed_path = file_path.replace("raw", "processed")
        os.makedirs(os.path.dirname(processed_path), exist_ok=True)
        df.to_csv(processed_path)
        print(f"✅ Indicadores calculados e salvos em {processed_path}")
        
        return df
    
    except Exception as e:
        print(f"❌ Erro ao calcular indicadores: {e}")
        return None

# Exemplo de uso
# calculate_indicators('data/raw/PETR4.SA.csv')