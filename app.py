from flask import Flask, render_template, request
import random

app = Flask(__name__)

DESTINATIONS = (
    ("Italia", "italia.png"),
    ("Tyskland", "tyskland.png"),
    ("Frankrike", "france.png"),
    ("Danmark", "danmark.png"),
    ("Sverige", "svergie.png"),
    ("USA", "usa.png"),
)


@app.route("/")
def main():
    return render_template("main.html", destinations=DESTINATIONS)

@app.route("/bestill", methods=["GET","POST"])
def bestill():
    turer = tuple(destination for destination, _image in DESTINATIONS)
    if request.method == "POST":
        gmail = request.form["gmail"]
        tur = request.form["tur"]
        tid = request.form["Lengde"]
        dato = request.form["dato"]
        person = request.form["person"]
        pris = random.randint(500, 10000)

        return render_template(
            "bestilling.html",
            gmail=gmail,
            tur=tur,
            pris=pris,
            dato=dato,
            person=person,
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