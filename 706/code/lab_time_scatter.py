from itertools import groupby
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

std_scale = preprocessing.StandardScaler().fit(subset[['VALUENUM']])
subset[['VALUENUM']] = std_scale.transform(subset[['VALUENUM']])


normal_labs = subset[subset['FLAG'] != 'abnormal']
abnormal_labs = subset[subset['FLAG'] == 'abnormal']

chart1 = alt.Chart(normal_labs).mark_circle(size=20).encode(
    x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
    color='Survival',
    tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
)

chart2 = alt.Chart(abnormal_labs).mark_circle(size=20).encode(
    x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
    color='Survival',
    tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
)

#band = alt.Chart(subset).mark_errorband(extent='ci').encode(
    #x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    #y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
#)

chart1 = chart1 + chart1.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()
chart2 = chart2 + chart2.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()

#sc_plot + sc_plot.transform_regression('temp_max', 'temp_min').mark_line()
st.write("### lab records within normal range")
st.altair_chart(chart1, use_container_width=True)

st.write("### lab records outside of normal range")
st.altair_chart(chart2, use_container_width=True)

