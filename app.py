from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/health')
def health():
    return "Healthy", 200

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80, debug=True)
    serve(app, host='0.0.0.0', port=80)
