from flask import Flask
app = Flask(__name__)
@app.route("/")
def erindex():
    return "<h1>The end</h1>"
app.run()
