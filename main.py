from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ekipler")
def ekipler():
    return render_template("ekipler.html")

@app.route("/paketler")
def paketler():
    return render_template("paketler.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

@app.route("/teklifal")
def teklifal():
    return redirect("https://discord.gg/JvTRYZdaQE")

if __name__ == "__main__":
    app.run()