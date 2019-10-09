from flask import Flask, render_template
import os

app = Flask(__name__)

# sometimes, the '/' url is also known the root url
@app.route('/')
def index():
    return render_template('index.template.html')
    
@app.route('/blog')
def show_blog():
    return render_template('blog.template.html')
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)