import altair as alt
import streamlit as st
import pandas as pd

st.write('Hello world!')

icu_labs = pd.read_csv('706/data/icu_lab.csv')

def label_death (row):
   if row['EXPIRE_FLAG'] == 1 :
      return 'Expired'
   return 'Survived'

icu_labs['Death'] = icu_labs.apply (lambda row: label_death(row), axis=1)


option = st.selectbox(
     'select lab',
     icu_labs.LABEL.unique())

subset = icu_labs[icu_labs["LABEL"] == option]

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    subset = subset[subset["Expire_Flag"] == 1]
elif death == 'Survived': 
    subset = subset[subset["Expire_Flag"] == 0]

chart = alt.Chart(subset).mark_circle(size=20).encode(
    x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU in mins'),
    y='VALUENUM',
    color='Death',
    #tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

st.altair_chart(chart, use_container_width=True)
