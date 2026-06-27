from flask import Flask

app=Flask(__name__)   #demo.py


@app.route("/")
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "aboutpage"

@app.route("/gallery")
def gallery():
    return "<h1>gallery</h1>"

if __name__=="__main__":
    app.run(debug=True,port=1234)