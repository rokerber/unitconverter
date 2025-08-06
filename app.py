from flask import Flask, render_template, request, send_from_directory

application = Flask(__name__)

# Nova rota para servir o arquivo sw.js na raiz do site.
# Isso é necessário para a verificação da Monetag.
@application.route('/sw.js')
def serve_sw():
    return send_from_directory('static', 'sw.js')

# Rota para a página inicial
@application.route('/')
def home():
    return render_template('index.html')

# Rota para a conversão de unidades
@application.route('/convert', methods=['POST'])
def convert():
    try:
        # Pega o valor do formulário e converte para um número inteiro
        bytes_value = int(request.form['bytes'])
        unit = request.form['unit']
        result = None

        # Realiza a conversão com base na unidade selecionada
        if unit == 'KB':
            result = f"{bytes_value / 1024:.2f} KB"
        elif unit == 'MB':
            result = f"{bytes_value / (1024 ** 2):.2f} MB"
        elif unit == 'GB':
            result = f"{bytes_value / (1024 ** 3):.2f} GB"
        elif unit == 'TB':
            result = f"{bytes_value / (1024 ** 4):.2f} TB"

        # Renderiza a página com o resultado da conversão
        return render_template('index.html', result=result)
    
    except (ValueError, KeyError):
        # Em caso de erro na entrada de dados, exibe uma mensagem de erro
        error_message = "Entrada inválida. Por favor, insira um número válido."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    application.run(debug=True)