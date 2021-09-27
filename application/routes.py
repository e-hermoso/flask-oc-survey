from application import app
from flask import render_template
# This could be the Root directory in the URL
# Note: These are called decorators. They decorate the underline definition or function.
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", index=True, loginUser=True)
@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/courses")
def courses():
    courseData = [{"errorId":"1111","error":"CR 2021-####","errordesc":"Message","potfixes":3,"issues":"three issues"},{"errorId":"1111","error":"CR 2021-####","errordesc":"Message","potfixes":3,"issues":"three issues"},{"errorId":"1111","error":"CR 2021-####","errordesc":"Message","potfixes":3,"issues":"three issues"}]

    return render_template("courses.html", courseData=courseData, courses=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)
