from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.adviceslip.com/advice')
    return render_template('index.html', advice=response.json()['slip']['advice'])