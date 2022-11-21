from flask import Flask, render_template


app = Flask(__name__)

@app.route('/url_name/<name>&<massage>')
def index(name, massage):
    return render_template('index.html', name=name, massage=massage)

@app.route('/')
def main():
    return "Main page"


if __name__ == '__main__': 
    app.run()