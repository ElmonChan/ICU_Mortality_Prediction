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

def label_death (row):
   if row['EXPIRE_FLAG'] == 1 :
      return 'Expired'
   return 'Survived'

df['Death'] = df.apply (lambda row: label_death(row), axis=1)

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    df = df[df["EXPIRE_FLAG"] == 1]
elif death == 'Survived': 
    df = df[df["EXPIRE_FLAG"] == 0]

base = alt.Chart(df)

bar1 = base.mark_bar().encode(
    x = alt.X('AGE_GROUP'),
    y = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','AGE_GROUP','EXPIRE_FLAG'],
    #column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different age groups",
    ).interactive(bind_y=True)

bar2 = base.mark_bar().encode(
    y = alt.Y('ETHNICITY'),
    x = 'count(SUBJECT_ID)',
    color = alt.Color('EXPIRE_FLAG:N'),
    tooltip = ['count(SUBJECT_ID)','ETHNICITY','EXPIRE_FLAG'],
    #row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
    ).properties(
        title= "population for different race groups",
    ).configure_axis(
    labelFontSize=5,
    labelAngle=45
    )

donut = base.mark_arc(innerRadius=50, outerRadius=90).encode(
    theta = alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
    color = alt.Color(field='GENDER', type='ordinal'),
    tooltip = ['sum(SUBJECT_ID)', 'AGE_GROUP']
    ).properties(
	title= "proportion of expired patients in gender",
	#width = 250
    )



bar1
donut
bar2