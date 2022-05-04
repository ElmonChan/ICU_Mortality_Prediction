from itertools import groupby
import altair as alt
import streamlit as st
import pandas as pd
from sklearn import preprocessing


def app():
    st.write("## Demographics of patients with abnormal lab values")
    st.write("This page allows exploration of demographics (age group and gender) for selected patients with abnormal lab values.")

    icu_labs = pd.read_csv('706/data/icuvalue_demo.csv')

    labs = list(icu_labs.LABEL.unique())
    default_ix = labs.index('Albumin')
    option = st.selectbox(
         'Select a lab test of interest here',
         labs,
         index = default_ix)

    subset = icu_labs[icu_labs["LABEL"] == option]

    death_choice = st.radio(
        "Select patient survival status here",
        ('All', 'Expired', 'Survived'))

    if death_choice == 'Expired':
        subset = subset[subset["Survival"] == death_choice]
    elif death_choice == 'Survived':
        subset = subset[subset["Survival"] == death_choice]

    unit = subset["VALUEUOM"].iloc[0]

    brush = alt.selection(type="interval")

    
    labs = alt.Chart(subset).mark_point(size=40).encode(
        x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=False), title='Time before admission to ICU (min)'),
        y= alt.Y ('VALUENUM', scale=alt.Scale(zero=False), title=f"Value ({unit})"),
        color=alt.condition(brush, 'Survival', alt.value('lightgray')),
        tooltip=['time_to_icu_mins', 'Survival']
    ).add_selection(
    brush
    ).properties(width=700, height=400, title="Abnormal lab values vs. time before admission to ICU")

    age = alt.Chart(subset).mark_bar().encode(
        y=alt.Y('AGE_GROUP:N', title='Age group'),
        x=alt.X(aggregate="count", axis=alt.Axis(tickMinStep=1), field='SUBJECT_ID', type='quantitative', title="Count of patients"),
        color=alt.Color('AGE_GROUP:N')
    ).transform_filter(brush
    ).properties(width=400, height=200, title="Patient age distribution")



    gender = alt.Chart(subset).mark_arc(innerRadius=50, outerRadius=90).encode(
            theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
            color=alt.Color('GENDER:N'),
            tooltip=['count(SUBJECT_ID)', 'GENDER'],
    ).transform_filter(brush
    ).properties(width=200, height=200, title="Patient gender distribution")



    demo = alt.hconcat(age, gender).properties(
    title="Demographics of selected patients",
    resolve = alt.Resolve(scale=alt.LegendResolveMap(color=alt.ResolveMode('independent')))
    )

    chart= alt.vconcat(labs, demo).properties(
    title="Lab values and patient demographics",
    resolve = alt.Resolve(scale=alt.LegendResolveMap(color=alt.ResolveMode('independent')))
    )
    st.altair_chart(chart)
  
    # band = alt.Chart(subset).mark_errorband(extent='ci').encode(
    #     x= alt.X('time_to_icu_mins', scale=alt.Scale(reverse=True), title = 'Time to ICU (min)'),
    #     y= alt.Y ('VALUENUM', title = f"Value ({unit})"),
    # )
    #sc_plot + sc_plot.transform_regression('temp_max', 'temp_min').mark_line()
    # st.write("### Lab records within normal range")
    # st.altair_chart(chart1)
    # st.write("### Lab records outside normal range")
    # st.altair_chart(chart2)


