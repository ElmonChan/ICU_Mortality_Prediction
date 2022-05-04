from itertools import groupby
import altair as alt
import streamlit as st
import pandas as pd
from sklearn import preprocessing


def app():
    st.write("## Lab results before ICU admissions")
    st.write("We hypothesized that being admitted to the ICU is a consequence of worsening conditions. This visualization is therefore created to help identify the relationship between lab values and ICU admissions (and survival status).")

    icu_labs = pd.read_csv('706/data/icu_lab.csv')

    labs = list(icu_labs.LABEL.unique())
    default_ix = labs.index('Albumin')
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

    # normal_labs = subset[subset['FLAG'] != 'abnormal']
    # abnormal_labs = subset[subset['FLAG'] == 'abnormal']

    # chart1 = alt.Chart(normal_labs).mark_circle(size=20).encode(
    #     x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time Before ICU Admission (min)'),
    #     y= alt.Y ('VALUENUM',  scale=alt.Scale(zero=False), title=f"Value ({unit})"),
    #     color='Survival',
    #     tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
    # )

    chart2 = alt.Chart(subset).mark_circle(size=20).encode(
        x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time Before ICU Admission (min)'),
        y= alt.Y ('VALUENUM', scale=alt.Scale(zero=False), title=f"Value ({unit})"),
        color='Survival',
        tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
    )

    # chart1 = chart1 + chart1.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()
    chart2 = chart2 + chart2.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()
    # chart1 = chart1.properties(width=800, height=600)
    chart2 = chart2.properties(width=800, height=600)

    #sc_plot + sc_plot.transform_regression('temp_max', 'temp_min').mark_line()
    # st.write("### lab value")
    st.altair_chart(chart2)
    # st.write("### lab records within normal range")
    # st.altair_chart(chart1)

