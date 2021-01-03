from flask import Flask, render_template, request, redirect



app = Flask(__name__)
app.config['SECRET_KEY'] = "bngdsljdsa94301ldvma"



@app.route("/")
def main():
    return render_template("index.html")



@app.route("/add/product", methods=['POST','GET'])
def create():
    return render_template('addProduct.html')


@app.route('/sign-up', methods=['POST','GET'])
def sign_up():
    return render_template('sign-up.html')


@app.route('/sign-in', methods=['POST','GET'])
def sign_in():
    return render_template('sign-in.html')

app.run(debug=True)