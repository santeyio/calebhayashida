from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")
