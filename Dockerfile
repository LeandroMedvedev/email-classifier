# 1. Ingrediente base: Comece com uma imagem oficial do Python.
# Use a mesma versão que você desenvolveu (ex: 3.10, 3.11).
FROM python:3.10-slim

# 2. Defina o diretório de trabalho dentro da "caixa".
ENV APP_HOME /app
WORKDIR $APP_HOME

# 3. Copie apenas o arquivo de dependências primeiro.
# Isso otimiza o build, aproveitando o cache.
COPY requirements.txt ./

# 4. Instale as dependências.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Agora, copie todo o resto do seu código para dentro da "caixa".
COPY . .

# 6. Comando final: O que deve ser executado quando a aplicação ligar.
# Substitua 'src.app:app' pelo caminho correto do seu objeto de aplicação ASGI/WSGI.
# O Gunicorn é um servidor de produção mais robusto que o Uvicorn sozinho.
# Adicione 'gunicorn' ao seu 'requirements.txt'.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "src.app:app", "-k", "uvicorn.workers.UvicornWorker"]