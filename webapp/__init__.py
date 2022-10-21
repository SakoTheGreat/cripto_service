from flask import Flask, render_template

from webapp.model import db



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    #with app.app_context():
        #db.create_all()

    @app.route('/')
    def index():
        title = 'P2P Scanner'
        return render_template('index.html', page_title=title, text=title)

    return app
