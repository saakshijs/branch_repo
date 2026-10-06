from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        food = request.form["food"]
        message = "Your " + food + " has been ordered! 🍕"

    return render_template("frontend.html", message=message)

app.run(debug=True)
