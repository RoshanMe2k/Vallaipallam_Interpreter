import os
from flask import Flask, render_template, request
from shell import main_shell

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    output = error= code = ""
    if request.method == "POST":
        code = request.form.get("code")
        output,error= main_shell(code)
        if error:
            output=''
    return render_template("index.html", code=code, output=output,error=error)

if __name__ == "__main__":
    app.run()
