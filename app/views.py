from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return 'About'

@app.route('/products')
def products():
	return 'Products'

@app.route('/team')
def team():
	return 'Team'

@app.route('/sample')
def sample():
	return 'Sample Research'

@app.route('/contact')
def contact():
	return 'Contact'