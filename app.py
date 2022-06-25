from flask import Flask, render_template, request
from forms import ContactForm

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'passwordsecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/aboutme', methods=['GET', 'POST'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/examplework', methods=['GET', 'POST'])
def examplework():
    return render_template('examplework.html')

@app.route('/Contactme', methods=['GET', 'POST'])
def contactme():
    return render_template('contactme.html', template_form=ContactForm())

