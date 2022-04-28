import altair as alt
import pandas as pd
import streamlit as st


def load_data():
    df = pd.read_csv("706/data/demographic.csv")
    return df
df = load_data()

#sex = st.radio('GENDER', ('M', 'F'))
#subset = df[df["Sex"] == sex]
status_selection = alt.selection_single(
    fields=['EXPIRE_FLAG'],
    #bind='legend'
)

bar = alt.Chart(df).mark_bar().encode(
    x = alt.X('AGE_GROUP'),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('GENDER'),
    tooltip = ['count(GENDER)', 'count(SUBJECT_ID)','AGE_GROUP']
    ).properties(
        title= "population for different age groups",
    ).add_selection(
        status_selection
    ).properties(
        width=150
    )
#.add_selection(age_selection)
#st.altair_chart(chart1, use_container_width=True)


donut = alt.Chart(df).mark_arc(innerRadius=50, outerRadius=90).encode(
    theta = alt.Theta(aggregate="count", field='EXPIRE_FLAGE', type='quantitative'),
    color = alt.Color(field='AGE_GROUP', type='ordinal'),
    tooltip = ['sum(EXPIRE_FLAG)', 'AGE_GROUP']
).properties(
    width=250
)

chart = alt.vconcat(bar, donut
).resolve_scale(
    color='independent'
)

chart