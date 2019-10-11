from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# the default is the GET method
@app.route('/countries')
def index():
    return {
        "sg":"Singapore",
        "my" : "Malaysia",
        "cn" : "China"
    }
    
@app.route('/')
def test_index():
    return render_template('test-api.html')

    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)