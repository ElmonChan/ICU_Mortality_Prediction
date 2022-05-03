from itertools import groupby
import altair as alt
import streamlit as st
import pandas as pd
from sklearn import preprocessing


def app():
    st.write("## Lab results Before ICU admission")
    st.write("This page help explore relationship between the lab result trend and the deteriorating physical condition. \
              We assume that ICU admission generally represent the worsening of condition. So we visualize the lab value \
              shortly before ICU admission")

    icu_labs = pd.read_csv('706/data/icu_lab.csv')

    labs = list(icu_labs.LABEL.unique())
    default_ix = labs.index('Cholesterol, Total')
    option = st.selectbox('Select a lab to study', labs, index=default_ix)

    subset = icu_labs[icu_labs["LABEL"] == option]

    death_choice = st.radio(
        "Select patients",
        ('All', 'Expired', 'Survived'))

    if death_choice == 'Expired':
        subset = subset[subset["Survival"] == death_choice]
    elif death_choice == 'Survived':
        subset = subset[subset["Survival"] == death_choice]

    unit = subset["VALUEUOM"].iloc[0]

    normal_labs = subset[subset['FLAG'] != 'abnormal']
    abnormal_labs = subset[subset['FLAG'] == 'abnormal']

    chart1 = alt.Chart(normal_labs).mark_circle(size=20).encode(
        x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time Before ICU Admission (min)'),
        y= alt.Y ('VALUENUM',  scale=alt.Scale(zero=False), title=f"Value ({unit})"),
        color='Survival',
        tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
    )

    chart2 = alt.Chart(abnormal_labs).mark_circle(size=20).encode(
        x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time Before ICU Admission (min)'),
        y= alt.Y ('VALUENUM', scale=alt.Scale(zero=False), title=f"Value ({unit})"),
        color='Survival',
        tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
    )

    chart1 = chart1 + chart1.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()
    chart2 = chart2 + chart2.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()
    chart1 = chart1.properties(width=800, height=600)
    chart2 = chart2.properties(width=800, height=600)

    #sc_plot + sc_plot.transform_regression('temp_max', 'temp_min').mark_line()
    st.write("### lab records outside normal range")
    st.altair_chart(chart2)
    st.write("### lab records within normal range")
    st.altair_chart(chart1)

