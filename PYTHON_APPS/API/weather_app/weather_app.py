from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/v1/api/<station>/<date>')
def api_data(station,date):
    temp = 46
    return {'station': station,'date':date,'temperature':temp}


if __name__ == '__main__':
    app.run(debug=True)




