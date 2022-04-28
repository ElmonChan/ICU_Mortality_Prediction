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

bar1 = alt.Chart(df).mark_bar().encode(
    x = alt.X('EXPIRE_FLAG:N',title=None, axis=alt.Axis(labels=False)),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','AGE_GROUP','EXPIRE_FLAG'],
    column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different age groups",
    )

bar2 = alt.Chart(df).mark_bar().encode(
    x = alt.X('EXPIRE_FLAG:N',title=None, axis=alt.Axis(labels=False)),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','AGE_GROUP','EXPIRE_FLAG'],
    column = alt.Column('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different age groups",
    )


donut = alt.Chart(df).mark_arc(innerRadius=50, outerRadius=90).encode(
    theta = alt.Theta(aggregate="count", field='EXPIRE_FLAGE', type='quantitative'),
    color = alt.Color(field='AGE_GROUP', type='ordinal'),
    tooltip = ['sum(EXPIRE_FLAG)', 'AGE_GROUP']
).properties(
    width=250
)

bar = alt.hconcat(bar1, bar2
).resolve_scale(
    color='independent'
)

chart = alt.vconcat(bar, donut
).resolve_scale(
    color='independent'
)

chart