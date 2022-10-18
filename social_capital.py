import streamlit as st
import pandas as pd
import plotly.express as px



df = pd.read_csv("social_capital.csv")
st.set_page_config(
    page_title="Birth Rates",
    page_icon="✅",
    layout="wide",
)

st.header('Birth Rates')


st.markdown("""---""")

option = st.selectbox(
    'Select !',
    (df.columns.values[2:])
)




chartChoropleth = px.choropleth(data_frame=df,
                        locations='STATE',
                        locationmode="USA-states",
                        scope="usa",
                        height=600,
                        width = 600,
                        color=option,
                        animation_frame='YEAR')

st.plotly_chart(chartChoropleth)

st.markdown("""---""")

st.write(df)