from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/bestill", methods=["GET","POST"])
def bestill():

    turer = ("Italia", "Frankrike", "Danmark", "Sverige", "USA")
    if request.method == "POST":
        gmail = request.form["gmail"]
        tur = request.form["tur"]
        tid = request.form["Lengde"]
        pris = random.randint(500, 4000)

        return render_template(
            "bestilling.html",
            gmail=gmail,
            tur=tur,
            pris=pris,
            tid=tid,
        )

    return render_template(
        "bestill.html",
        turer=turer,
    )

@app.route("/om")
def om():
    return render_template("om.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)