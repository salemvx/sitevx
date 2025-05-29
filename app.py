import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")

@app.route("/ia")
def ia():
    return render_template("ia.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route('/politica-de-privacidade')
def privacy():
    return render_template('privacy.html')

@app.route('/termos-de-uso')
def termos():
    return render_template('terms.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
