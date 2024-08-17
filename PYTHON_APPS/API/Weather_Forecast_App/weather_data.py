import requests


API_KEY= '141710af2113bab9f55ef73e1bcd33d5'

def get_data(place,forecast_days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid=141710af2113bab9f55ef73e1bcd33d5'
    response = requests.get(url)
    raw_data = response.json()
    data = raw_data['list']
    forecast_days_values = 8 * forecast_days
    real_data = data[:forecast_days_values]
    return real_data

if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3))



