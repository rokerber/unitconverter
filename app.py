from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
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

if __name__ == '__main__':
    app.run(debug=True)