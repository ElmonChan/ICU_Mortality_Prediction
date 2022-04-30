import altair as alt
import streamlit as st
import pandas as pd

st.write("## Lab results Before ICU admission")

icu_labs = pd.read_csv('706/data/icu_lab.csv')

option = st.selectbox(
     'select lab',
     icu_labs.LABEL.unique(), 
     default='Alkaline Phosphatase')

subset = icu_labs[icu_labs["LABEL"] == option]

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    subset = subset[subset["Survival"] == death]
elif death == 'Survived': 
    subset = subset[subset["Survival"] == death]

unit = subset["VALUEUOM"].iloc[0]


chart = alt.Chart(subset).mark_circle(size=20).encode(
    x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    y= alt.Y ('VALUENUM', title = f"Value ({unit})", scale=alt.Scale(type='log', base = 2)),
    color='Survival',
    tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
).interactive()


#chart = chart + chart.transform_regression('time_to_icu_mins', 'VALUENUM').mark_line()

st.altair_chart(chart, use_container_width=True)
