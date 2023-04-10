from flask import Flask, render_template

app = Flask ('__name__')

@app.route("/")
def home ():
    return render_template ("home.html")

@app.route("/qmsomos")
def qm_somos ():
    return render_template ("qmsomos.html")

@app.route("/contato")
def contato_ ():
    return render_template ("contato.html")