from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h3>Hello, World</h3>"

@app.route('/hello')
def hellow():
    return "<h3>Hello</h3>"

@app.route('/goodbye')
def goodbye():
    return "<h3>Goodbye</h3>"

if __name__ == "__main__":
    app.run(debug=True)