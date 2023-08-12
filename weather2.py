import streamlit as st
import requests
api_key="0d20fb377a8095772ff0ab7db929e770"

def convert(name):
    return name-273.15
def weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    weather_data=requests.get(url).json()
    
    general=weather_data['weather'][0]['main']
    icon_id=weather_data['weather'][0]['icon']
    temperature=round(convert(weather_data['main']['temp']))
    icon=f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return general,temperature,icon

                      
st.header("Weather Forecast")
city1=st.text_input("Enter the city").lower()
if st.button("Show Weather"):
    gerneral,temperature,icon=weather(city1)
    col1,col2=st.columns(2)
    with col1:
        st.metric(label="Temperature",value=f"{temperature}°C")
    with col2:
        st.title(gerneral)
        st.image(icon)
