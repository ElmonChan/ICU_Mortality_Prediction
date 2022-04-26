import altair as alt
import pandas as pd
import streamlit as st


def load_data():
    df = pd.read_csv("706/data/demographic.csv")
    return df
df = load_data()

#sex = st.radio('GENDER', ('M', 'F'))
#subset = df[df["Sex"] == sex]

bar = alt.Chart(df).mark_bar().encode(
    x = alt.X('AGE_GROUP'),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('GENDER'),
    #opacity = alt.condition(age_selection, alt.value(1), alt.value(0.2))
    ).properties(
        title= "population for different age groups",
    )
#.add_selection(age_selection)
st.altair_chart(chart1, use_container_width=True)


donut = base.mark_arc(innerRadius=50, outerRadius=90).encode(
    theta = alt.Theta(aggregate="sum", field='EXPIRE_FLAGE', type='quantitative'),
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