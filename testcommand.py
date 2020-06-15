from flask import Flask
testname = Flask(__name__)

@app.route("/")
def hello():
    return "Hey Continuous tEST!"
