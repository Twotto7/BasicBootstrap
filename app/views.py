from flask import render_template
from app import app
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/example')
def example():
    return render_template('example.html')

