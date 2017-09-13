from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

def test():
    print 'something'
    print 'something else'
