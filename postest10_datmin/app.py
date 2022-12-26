from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == "POST":
        bil1 = int(request.form['bil1'])
        bil2 = int(request.form['bil2'])
        hasil = f'{bil1} + {bil2} = {bil1+bil2}'
    else:
        hasil = " _ + _ = _"
    return render_template('index.html', hasil=hasil)


if __name__ == "__main__":
    app.run(debug=True)