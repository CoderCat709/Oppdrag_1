from flask import Flask, render_template, request
import random

app = Flask(__name__)
number = random.randint(500, 4000) 


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/bestill", methods=["GET","POST"])
def bestill():

    turer = ("Italia","Frankrie","Danmark","Sverige","USA") 
    priser = ()

    
    if request.method == "POST":
        gmail = request.form["gmail"]
        tur = request.form["tur"]
        pris = request.form.get["x"]
        kommentar = request.form.get("kommentar", "")

        return render_template(
            "bestilling.html",
            tur=tur,
            pris=pris,
            kommentar=kommentar
        )
    return render_template(
    "bestill.html",
    turer=turer,
    )
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/om")
def om():
    return render_template("om.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")
    


if __name__ == "__main__":
    app.run(debug=True)