import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

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

    df['GENDER'] = df['GENDER'].map({'F': 'Female', 'M': 'Male'})
    return df
df = load_data()

def label_death (row):
   if row['EXPIRE_FLAG'] == 1 :
      return 'Expired'
   return 'Survived'

df['Death'] = df.apply (lambda row: label_death(row), axis=1)



with st.sidebar:
    group_choice = st.radio(
        "select patients",
        ( 'Gender', 'Expired/Survived', 'All')
    )

# if death == 'Gender':
#     df = df[df["EXPIRE_FLAG"] == 1]
# elif death == 'Survived':
#     df = df[df["EXPIRE_FLAG"] == 0]

base = alt.Chart(df)

if group_choice == 'Gender':
    bar1 = base.mark_bar().encode(
        x = alt.X('count(SUBJECT_ID)'),
        y = alt.Y('AGE_GROUP'),
        color = alt.Color('GENDER:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
        tooltip = ['count(SUBJECT_ID)','AGE_GROUP','GENDER:N'],
        #column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
        ).interactive(bind_y=True)

    bar2 = base.mark_bar().encode(
        y=alt.Y('ETHNICITY', sort='-x'),
        x=alt.X('count(SUBJECT_ID)'),
        color=alt.Color('GENDER:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
        tooltip=['count(SUBJECT_ID)', 'ETHNICITY', 'GENDER:N'],
        # row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
    )

    donut = base.mark_arc(innerRadius=50, outerRadius=90).encode(
        theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
        color=alt.Color('GENDER:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
        tooltip=['count(SUBJECT_ID)', 'GENDER'],
    )
elif group_choice == 'Expired/Survived':
    bar1 = base.mark_bar().encode(
        x='count(SUBJECT_ID)',
        y=alt.Y('AGE_GROUP'),
        color=alt.Color('Death'),
        tooltip=['count(SUBJECT_ID)', 'AGE_GROUP', 'Death'],
        # column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
    ).interactive(bind_y=True)

    bar2 = base.mark_bar().encode(
        y=alt.Y('ETHNICITY', sort='-x'),
        x=alt.X('count(SUBJECT_ID)'),
        color=alt.Color('Death'),
        tooltip=['count(SUBJECT_ID)', 'ETHNICITY', 'Death'],
        # row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
    )
    donut = base.mark_arc(innerRadius=50, outerRadius=90).encode(
        theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
        color=alt.Color(field='Death', type='ordinal'),
        tooltip=['count(SUBJECT_ID)', 'Death']
    )
else:
    bar1 = base.mark_bar().encode(
        x='count(SUBJECT_ID)',
        y=alt.Y('AGE_GROUP'),
        tooltip=['count(SUBJECT_ID)', 'AGE_GROUP'],
        # column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
    ).interactive(bind_y=True)

    bar2 = base.mark_bar().encode(
        y=alt.Y('ETHNICITY', sort='-x'),
        x=alt.X('count(SUBJECT_ID)'),
        tooltip=['count(SUBJECT_ID)', 'ETHNICITY'],
        # row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
    )





bar1 = bar1.properties(
            title="Population for different age groups",
            width=400,
            height=300
        )
bar2 = bar2.properties(
        title="Population for different race groups",
        width=450,
        height=300
    )

if group_choice != 'All':
    donut = donut.properties(
            title="Proportion of expired patients in gender",
            width=400
        )
    bar1|bar2|donut
else:
    bar1|bar2
