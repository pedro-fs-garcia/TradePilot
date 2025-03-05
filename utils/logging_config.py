import logging
import os
from logging.handlers import RotatingFileHandler

# Cria a pasta logs se ela não existir
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configuração básica de logging
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)

# Tamanho máximo do arquivo de log (10 MB)
max_log_size = 10 * 1024 * 1024  # 10 MB
backup_count = 5  # Número de arquivos de log antigos a manter

# Handler para o log geral
general_handler = RotatingFileHandler(
    "logs/app.log", maxBytes=max_log_size, backupCount=backup_count
)
general_handler.setLevel(logging.INFO)
general_handler.setFormatter(formatter)

# Handler para o log de erros
error_handler = RotatingFileHandler(
    "logs/error.log", maxBytes=max_log_size, backupCount=backup_count
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Handler para saída no terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# Configuração do logger principal
app_logger = logging.getLogger("app")
app_logger.setLevel(logging.INFO)
app_logger.addHandler(general_handler)
app_logger.addHandler(error_handler)
app_logger.addHandler(stream_handler)

# Logger específico para erros (opcional, se quiser separar ainda mais)
error_logger = logging.getLogger("app.error")
error_logger.setLevel(logging.ERROR)
error_logger.addHandler(error_handler)

## exemplo de uso
# app_logger.info("Esta é uma mensagem de informação.")
# app_logger.error("Esta é uma mensagem de erro.")
# error_logger.error("Esta é uma mensagem de erro específica.")