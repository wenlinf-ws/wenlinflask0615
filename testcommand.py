from flask import Flask
test = Flask(__name__)

@test.route("/")
def hello():
    return "Hey Continuous tEST!"
