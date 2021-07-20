from flask import Flask, render_template
app=Flask(__name__)

# creating main route, with name and dynamic name paths 

@app.route("/")
def index():
    name="Default"
    return render_template("sample1.html", n=name)

@app.route("/<name>")
def sample(name):
    hobbies=["playing Cricket","Watching Movies","Listening Music"]
    return render_template("sample1.html", n=name, h=hobbies)

