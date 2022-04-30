import altair as alt
import pandas as pd
import streamlit as st


def load_data():
    df = pd.read_csv("706/data/demographic.csv")
    return df
df = load_data()

conditions = [
    (df['ETHNICITY'].contains('WHITE'),
    (df['ETHNICITY'].contains('BLACK'),
    (df['ETHNICITY'].contains('ASIAN'),
    (df['ETHNICITY'].contains('UNKNOWN'),
    !(df['ETHNICITY'].contains('UNKNOWN') & !(df['ETHNICITY'].contains('ASIAN') & !(df['ETHNICITY'].contains('BLACK') & !(df['ETHNICITY'].contains('WHITE')
    ]
values = ['WHITE', 'BLACK', 'ASIAN', 'UNKNOWN', 'OTHER']
df['RACE'] = np.select(conditions, values)
#sex = st.radio('GENDER', ('M', 'F'))
#subset = df[df["Sex"] == sex]


bar1 = alt.Chart(df).mark_bar().encode(
    x = alt.X('EXPIRE_FLAG:N',title=None, axis=alt.Axis(labels=False)),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','AGE_GROUP','EXPIRE_FLAG'],
    column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different age groups",
    ).interactive(bind_y=True)

bar2 = alt.Chart(df).mark_bar().encode(
    y = alt.Y('EXPIRE_FLAG:N',title=None, axis=alt.Axis(labels=False)),
    x = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','AGE_GROUP','EXPIRE_FLAG'],
    row = alt.Row('RACE', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different race groups",
    )


donut = alt.Chart(df).mark_arc(innerRadius=50, outerRadius=90).encode(
    theta = alt.Theta(aggregate="count", field='EXPIRE_FLAGE', type='quantitative'),
    color = alt.Color(field='AGE_GROUP', type='ordinal'),
    tooltip = ['sum(EXPIRE_FLAG)', 'AGE_GROUP']
).properties(
	width = 250
    )

#bar1 & bar2.properties(df.sample(df.shape[0]))
chart = alt.vconcat(bar1, donut
).resolve_scale(
    color='independent'
)

chart
bar2