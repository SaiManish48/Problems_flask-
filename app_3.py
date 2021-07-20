from flask import Flask, render_template, request
app=Flask(__name__)

# creating main route, with name and dynamic name paths 

@app.route("/")
def index():
    return render_template("sample2.html")

@app.route("/sample", methods=['GET','POST'])
def sample():
    if request.method=="GET":
        name="Default"
    else:
        name=request.form.get('fname')
    hobbies=["playing Cricket","Watching Movies","Listening Music"]
    return render_template("sample_1.html", n=name, h=hobbies)

