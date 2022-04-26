import altair as alt
import pandas as pd
import streamlit as st


def load_data():
    df = pd.read_csv("706/data/demographic.csv")
    return df
df = load_data()

#sex = st.radio('GENDER', ('M', 'F'))
#subset = df[df["Sex"] == sex]

chart1 = alt.Chart(df).mark_bar().encode(
    x = alt.X('AGE_GROUP'),
    y = 'count('EXPIRE_FLAG'):Q',
    # color = alt.Color('Age',sort=ages),
    #opacity = alt.condition(age_selection, alt.value(1), alt.value(0.2))
    ).properties(
        title= "population for different age groups",
    )
#.add_selection(age_selection)
st.altair_chart(chart1, use_container_width=True)

