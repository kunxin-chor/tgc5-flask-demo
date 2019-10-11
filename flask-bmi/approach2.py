from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# the default is the GET method
@app.route('/bmi', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.template.html")
    elif request.method == "POST":
        # the key we use is the name attribute of the input
        weight = float(request.form['weight'])
        height = float(request.form['h'])
        bmi = weight / (height * height)
        return "BMI = " + str(bmi)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)