from itertools import groupby
import altair as alt
import streamlit as st
import pandas as pd
from sklearn import preprocessing


def app():
    st.write("## Lab results Before ICU admission")

    icu_labs = pd.read_csv('706/data/icu_lab.csv')

    labs = list(icu_labs.LABEL.unique())
    default_ix = labs.index('Cholesterol, Total')
    option = st.selectbox(
         'select lab',
         labs,
         index = default_ix)

    subset = icu_labs[icu_labs["LABEL"] == option]

    # death_choice = alt.selection(type='single',fields=['Survival'], init={'Survival':'Expired'})

    # numRecordsChart = alt.Chart(subset).mark_bar(width=30).encode(
    #     x= alt.X('Survival'),
    #     y= alt.Y('count()', title = "Number of records"),
    #     color=alt.condition(death_choice, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
    #     # tooltip=['FLAG', 'time_to_icu_mins', 'Survival']
    # ).add_selection(
    #     death_choice
    # ).properties(
    #     width=500,
    #     height=500
    # )
    # st.altair_chart(numRecordsChart)

    death_choice = st.radio(
        "Select patients",
        ('All', 'Expired', 'Survived'))

    if death_choice == 'Expired':
        subset = subset[subset["Survival"] == death_choice]
    elif death_choice == 'Survived':
        subset = subset[subset["Survival"] == death_choice]

    unit = subset["VALUEUOM"].iloc[0]

    #std_scale = preprocessing.StandardScaler().fit(subset[['VALUENUM']])
    #subset[['VALUENUM']] = std_scale.transform(subset[['VALUENUM']])


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

    # band = alt.Chart(subset).mark_errorband(extent='ci').encode(
    #     x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    #     y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
    # )

    chart1 = chart1 + chart1.transform_regression('time_to_icu_mins', 'VALUENUM', groupby=['Survival']).mark_line()
    chart2 = chart2 + chart2.transform_regression(
        'time_to_icu_mins', 'VALUENUM', groupby=['Survival']
        ).mark_line()

    chart1 = chart1.properties(
        width=800,
        height=600
    )

    chart2 = chart2.properties(
        width=800,
        height=600
    )

    #sc_plot + sc_plot.transform_regression('temp_max', 'temp_min').mark_line()
    st.write("### lab records outside of normal range")
    st.altair_chart(chart2)
    st.write("### lab records within normal range")
    st.altair_chart(chart1)

