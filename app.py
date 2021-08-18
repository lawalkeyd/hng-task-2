from flask import Flask, request , render_template

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def index(name='waiting for input'):
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name)    
    return render_template('index.html', name=name)    