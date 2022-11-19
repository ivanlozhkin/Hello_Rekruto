from flask import Flask


app = Flask(__name__)

@app.route('/url_name/<name>&<massage>')
def url_name(name, massage):
    return f"Hello {name}! {massage}!"


if __name__ == '__main__':
    app.run()