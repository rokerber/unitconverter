import sys
import os

# Pega o caminho do diretório onde o wsgi.py está.
# O log nos diz que é '/var/www/webroot/ROOT/'
path = os.path.dirname(os.path.abspath(__file__))

# Adiciona o caminho ao sys.path para que o Python consiga encontrar app.py
if path not in sys.path:
    sys.path.append(path)

# Importa a nossa aplicação
from app import application

# Este bloco não é necessário para a produção com mod_wsgi,
# mas pode ser útil se você rodar o wsgi.py diretamente.
if __name__ == "__main__":
    application.run()