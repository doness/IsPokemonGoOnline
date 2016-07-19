from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from availability import messages, Availability

@app.route("/", methods=["GET","POST"])
def homeFunc():
    mesgs = ["Run and get your Pikachu!", "The servers are unstable! Be careful!", "Servers are not working! Wait some few minutes!", "It's a good time to play"]
    statusmesg = mesgs[messages().PingMessage()]
    pingmesg = Availability().IPGOOAvailable()
    pingmesg = int(float(pingmesg))
    return render_template("home.html", status=statusmesg, ping=pingmesg)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
