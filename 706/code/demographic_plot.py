""" import altair as alt
import pandas as pd
import streamlit as st


def load_data():
    ## {{ CODE HERE }} ##
    cancer_df = pd.read_csv("https://github.com/ElmonChan/ICU_Mortality_Prediction/tree/main/706/data/demographic.csv")
    return df
df = load_data()

sex = st.radio('GENDER', ('M', 'F'))
subset = df[df["Sex"] == sex]

chart1 = chart.mark_bar().encode(
    x = alt.X('AGE_GROUP'),
    y = alt.Y('Pop'),
    # color = alt.Color('Age',sort=ages),
    opacity = alt.condition(age_selection, alt.value(1), alt.value(0.2)
    )).properties(
        title=f" population for different age groups",
    )
#.add_selection(age_selection)
st.altair_chart(chart1, use_container_width=True) """

import streamlit as st
st.write("hello")