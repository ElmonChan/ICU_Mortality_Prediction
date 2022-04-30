import altair as alt
import streamlit as st
import pandas as pd

st.write('Hello world!')

icu_labs = pd.read_csv('706/data/icu_lab.csv')

option = st.selectbox(
     'select lab',
     icu_labs.LABEL.unique())

subset = icu_labs[icu_labs["LABEL"] == option]

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    subset = subset[subset["EXPIRE_FLAG"] == 1]
elif death == 'Survived': 
    subset = subset[subset["EXPIRE_FLAG"] == 0]

alt.Chart(subset).mark_circle(size=20).encode(
    x='time_to_icu_mins',
    y='VALUENUM',
    #color='Origin',
    #tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

#st.altair_chart(chart, use_container_width=True)
