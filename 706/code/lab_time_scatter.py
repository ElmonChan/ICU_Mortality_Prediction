import altair as alt
import streamlit as st
import pandas as pd
from sklearn import preprocessing



st.write("## Lab results Before ICU admission")

icu_labs = pd.read_csv('706/data/icu_lab.csv')

option = st.selectbox(
     'select lab',
     icu_labs.LABEL.unique(), 
     index = 1)

subset = icu_labs[icu_labs["LABEL"] == option]

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    subset = subset[subset["Survival"] == death]
elif death == 'Survived': 
    subset = subset[subset["Survival"] == death]

unit = subset["VALUEUOM"].iloc[0]

std_scale = preprocessing.MinMaxScaler().fit(subset[['VALUENUM']])
subset[['VALUENUM']] = std_scale.transform(subset[['VALUENUM']])

chart = alt.Chart(subset).mark_circle(size=20).encode(
    x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
    color='FLAG',
    tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
).interactive()

#band = alt.Chart(subset).mark_errorband(extent='ci').encode(
    #x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    #y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
#)


#chart = chart + chart.transform_regression('time_to_icu_mins', 'VALUENUM').mark_line()

st.altair_chart(chart, use_container_width=True)
