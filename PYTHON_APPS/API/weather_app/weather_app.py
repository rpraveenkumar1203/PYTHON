from flask import Flask ,render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')

def home_page():
    return render_template('home.html')

@app.route('/v1/api/<station>/<date>')

def weather_api_help_page(station,date):
    data = 'weather_data/data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(data,skiprows=20,parse_dates=['    DATE'])
    temp = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    #print(temp)
    return {'date':date,'station':station,'temperature':temp}

if __name__ == '__main__':
    app.run(debug=True)
