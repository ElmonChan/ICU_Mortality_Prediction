import altair as alt
import pandas as pd
import streamlit as st
import numpy as np


def load_data():
    df = pd.read_csv("706/data/demographic.csv")
    df['ETHNICITY'] = df['ETHNICITY'].apply(lambda x: x.split('/')[0])
    df['ETHNICITY'] = df['ETHNICITY'].apply(lambda x: x.split('-')[0])
    df.replace('UNALBE', 'UNKNOWN')
    df[df['ETHNICITY'] == 'PATIENT']['ETHNICITY'] = 'UNKNOWN'
    df[df['ETHNICITY'] == 'MIDDLE']['ETHNICITY'] = 'OTHER'
    df[df['ETHNICITY'] == 'MULTI']['ETHNICITY'] = 'OTHER'
    df[df['ETHNICITY'] == 'NATIVE']['ETHNICITY'] = 'OTHER'
    df[df['ETHNICITY'] == 'SOUTH']['ETHNICITY'] = 'OTHER'
    df[df['ETHNICITY'] == 'PORTUGUESE']['ETHNICITY'] = 'OTHER'
    df[df['ETHNICITY'] == 'CARIBBEAN']['ETHNICITY'] = 'OTHER'
    df[df['ETHNICITY'] == 'AMERICAN']['ETHNICITY'] = 'OTHER'
    return df
df = load_data()

expire = [0,1]
expire_dropdown = alt.binding_select(options=expire)
expire_select = alt.selection_single(fields=['EXPIRE_FLAG'], bind=expire_dropdown,  init={'EXPIRE':expire[0]})
#sex = st.radio('GENDER', ('M', 'F'))
#subset = df[df["Sex"] == sex]

base = alt.Chart(df)

bar1 = base.encode(
    x = alt.X('AGE_GROUP',title=None, axis=alt.Axis(labels=False)),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','AGE_GROUP','EXPIRE_FLAG'],
    column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
    ).add_selector(
	expire_select
    ).properties(
        title= "population for different age groups",
    ).interactive(bind_y=True)

bar2 = base.mark_bar().encode(
    y = alt.Y('EXPIRE_FLAG:N',title=None, axis=alt.Axis(labels=False)),
    x = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','EXPIRE_FLAG'],
    row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different race groups",
    )


donut = base.mark_arc(innerRadius=50, outerRadius=90).encode(
    theta = alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
    color = alt.Color(field='GENDER', type='ordinal'),
    tooltip = ['sum(SUBJECT_ID)', 'AGE_GROUP']
    ).properties(
	title= "proportion of expired patients in gender",
	#width = 250
    )

#bar1 & bar2.properties(df.sample(df.shape[0]))


bar1
donut
bar2