from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'P2P Scanner'
    return render_template('index.html', page_title=title, text=title)


if __name__ == '__main__':
    app.run(debug=True)