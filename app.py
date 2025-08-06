from flask import Flask, render_template, request, send_from_directory

application = Flask(__name__)

# Rota para servir o arquivo sw.js na raiz do site.
# Isso permite que a Monetag encontre e verifique o arquivo.
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
        bytes_value = int(request.form['bytes'])
        unit = request.form['unit']
        result = None

        if unit == 'KB':
            result = f"{bytes_value / 1024:.2f} KB"
        elif unit == 'MB':
            result = f"{bytes_value / (1024 ** 2):.2f} MB"
        elif unit == 'GB':
            result = f"{bytes_value / (1024 ** 3):.2f} GB"
        elif unit == 'TB':
            result = f"{bytes_value / (1024 ** 4):.2f} TB"

        return render_template('index.html', result=result)
    
    except (ValueError, KeyError):
        error_message = "Entrada inválida. Por favor, insira um número válido."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    application.run(debug=True)