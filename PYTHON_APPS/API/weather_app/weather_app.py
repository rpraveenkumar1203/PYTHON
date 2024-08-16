from flask import Flask ,render_template
import pandas as pd

app = Flask(__name__)

stations = 'weather_data/data_small/stations.txt'
station_data = pd.read_csv(stations,skiprows=17)
station_data = station_data[['STAID','STANAME                                 ']].to_html()


@app.route('/')

def home_page():
    return render_template('home.html',data=station_data)

@app.route('/v1/api/<station>/<date>')

def weather_api_temp(station,date):
    data = 'weather_data/data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(data,skiprows=20,parse_dates=['    DATE'])
    temp = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    #print(temp)
    return {'date':date,'station':station,'temperature':temp}


@app.route('/v1/api/<station>')

def weather_api_station(station):
    data = 'weather_data/data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(data,skiprows=20,parse_dates=['    DATE'])
    result = df.to_dict(orient='records')
    return result



@app.route('/v1/api/<station>/<year>')

def weather_api_year(station,year):
    data = 'weather_data/data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(data,skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return result

if __name__ == '__main__':
    app.run(debug=True)



