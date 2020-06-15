from flask import Flask
testAppName = Flask(__name__)

@app.route("/")
def hello():
    return "Hey Continuous tEST!"
