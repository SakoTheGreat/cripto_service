from flask import Flask, render_template

from model import db



app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)

@app.route('/')
def index():
    title = 'P2P Scanner'
    return render_template('index.html', page_title=title, text=title)


if __name__ == '__main__':
    app.run(debug=True)
