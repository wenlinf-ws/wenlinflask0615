from flask import Flask
test = Flask(__name__)

@app.route("/")
def hello():
    return "Hey Continuous tEST!"
