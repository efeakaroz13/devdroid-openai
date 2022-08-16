from flask import Flask,render_template,request,redirect
from flask_cors import CORS
from devdroid import DevDroid
app = Flask(__name__)
@app.route("/")
def index():
    name= request.args.get("name")
    programminglanguages_q = request.args.get("prog")
    programminglanguages = programminglanguages_q.strip().split(";")

    devdroidai = DevDroid(name, programminglanguages=programminglanguages)

    return render_template("index.html",welcome=devdroidai.welcometext)

if __name__ == "__main__":
    app.run(debug=True)