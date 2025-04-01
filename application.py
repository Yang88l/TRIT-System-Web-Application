from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.form.get('name')
    headline="Welcome to the TRIT System Web Application"
    return render_template('index.html',  headline=headline)

@app.route('/about')
def about():
    return "This is the TRIT System Web Application. It helps in managing and analyzing data."

@app.route('/<string:name>')
def get_name(name):
    return f"<h1>Hello, {name}!</h1>"