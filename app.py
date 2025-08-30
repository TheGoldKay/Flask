from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello There!</p>"

@app.route("/about")
def about_page():
    return "<p>About Page</p>"

@app.route("/greetings/<int:index>")
def greeting(index):
    with open("greetings.json", 'r') as f:
        greetings = json.load(f).get("greetings")
        return f"<p>{greetings[index]}</p>"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"<p>{num1 + num2}</p>"

@app.route("/append/<string:phrase>")
def new_greeting(phrase):
    # the commented part is for dict_greetings.json
    with open("list_greetings.json", 'r') as f:
        data = json.load(f)
        #greetings = data.get("greetings")
    #greetings.append(phrase)
    #data["greetings"] = greetings
    #data["greetings"].append(phrase)
    data.append(phrase)
    with open("list_greetings.json", 'w') as f:
        json.dump(data, f, indent=4)
    return f"<p>{phrase}</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)