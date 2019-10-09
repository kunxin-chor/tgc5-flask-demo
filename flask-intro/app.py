from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# routing is the process mapping an URL to a function
@app.route('/')
def hello():
    name = "Paul"
    return render_template('index.template.html', first_name = name)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)