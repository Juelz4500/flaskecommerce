from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bike')
def bike():
    return render_template('bike.html') 

@app.route('/hamster')
def hamster():
    return render_template('hamster.html')

@app.route('/cubanlink')
def cubanlink():
    return render_template('cubanlink.html')

@app.route('/sc')
def sc():
    return render_template('sc.html')

@app.route('/lambo')
def lambo():
    return render_template('lambo.html')

@app.route('/pb')
def pb():
    return render_template('pb.html')

