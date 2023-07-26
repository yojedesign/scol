import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.sidebar.header('Cyberawareness Prediction App')
st.sidebar.subheader('Heatmap Parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut Chart Parameter')
donut_theta = st.sidebar.selectbox('Select data', ('s1', 's2'))

st.sidebar.subheader('Line Chart Parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Schooly](https://www.theschooly.co/).
''')
                    
# Row A

st.markdown('### Cyberawareness Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Phishing Attempts", "22", "+10%")
col2.metric("Security Training", "85%", "+5%")
col3.metric("Password Strength", "Strong", "+30")

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Heatmap')
    fig = px.histogram(
        data_frame=seattle_weather,
        x='date',
        color=time_hist_color,
        histfunc='median',
        height=345)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown('### Donut Chart')
    fig = px.pie(
        data_frame=stocks,
        names='company',
        values=donut_theta,
        hole=0.5)
    st.plotly_chart(fig, use_container_width=True)

# Row C
st.markdown('### Line Chart')
fig = px.line(
    data_frame=seattle_weather,
    x='date',
    y=plot_data,
    height=plot_height)
st.plotly_chart(fig)
