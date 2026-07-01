from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/name/<str>')
def name(str):
    str="Hello"
    return "My name is %s" % str

@app.route('/age/<int:n>')
def age(n):
    return "My age is %d" % n

if __name__ == '__main__':
    app.run(debug=True,port=1000)

