import streamlit as st
import plotly.express as px
import weather_data as wd
import pandas as pd

st.set_page_config(page_title='Weather Forecast App', layout='wide')
st.title('Weather Forecast for the Next Days')

place = st.text_input('Enter the city : ')

number_of_days = st.slider('Please enter the number of days to be foreacasted',min_value=1,max_value=5,help="Select the number of forecasted days")

#print(number_of_days)

forecast_type = st.selectbox('Select data to view :',('Temperature','Sky'))


if place :
        try :
            temperature_data = wd.get_data(place,number_of_days)
            st.subheader(f"Weather forecast next {number_of_days} days in {place.title()}")


            if forecast_type == 'Temperature':        
                temperature = [temperature['main']['temp'] - 273.15 for temperature  in temperature_data]
                #print(temperature_data)
                dates = [date['dt_txt']for date in temperature_data]
                print(dates)
                graph = px.line(x= dates ,y=temperature ,labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(graph,use_container_width=True)

            if forecast_type == 'Sky':

                images = {
                    "Clear": "https://raw.githubusercontent.com/rpraveenkumar1203/PYTHON/main/PYTHON_APPS/API/Weather_Forecast_App/images/clear.png",
                    "Clouds": "https://raw.githubusercontent.com/rpraveenkumar1203/PYTHON/main/PYTHON_APPS/API/Weather_Forecast_App/images/cloud.png",
                    "Rain": "https://raw.githubusercontent.com/rpraveenkumar1203/PYTHON/main/PYTHON_APPS/API/Weather_Forecast_App/images/rain.png",
                    "Snow": "https://raw.githubusercontent.com/rpraveenkumar1203/PYTHON/main/PYTHON_APPS/API/Weather_Forecast_App/images/snow.png"
                }

                weather_conditions = [sky['weather'][0]['main']for sky in temperature_data]
                image_paths = [images[condition] for condition in weather_conditions]
                dates = [date['dt_txt'] for date in temperature_data]
                st.image(image_paths, width=115,caption=dates)

        except KeyError:
             st.write('That place does not exist')