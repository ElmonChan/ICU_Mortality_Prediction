#from tkinter.tix import COLUMN
import pandas as pd
import altair as alt
import streamlit as st
import numpy as np

def app():

    st.write("## Distribution of patient demographics")
    st.write("We included a total of 10,282 patients in this study/visualization. To explore the distribution of patient demographics, select the choices below.")
    group_choice = st.radio(
        "Select the type of demographics to view:",
        ('Age Group', 'Gender', 'Race', 'Insurance', 'Religion', 'Marital Status')
    )
    st.markdown("""---""")

    ################# Demographic ######################
    df = pd.read_csv("src/data/demographic_new.csv")
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
    df['Survival'] = df['EXPIRE_FLAG'].map({0: 'Survived', 1: 'Expired'})
    
    #df.columns = df.columns.str.strip()
    df['ETHNICITY'] = df['ETHNICITY'].str.strip()

    WIDTH = 600

    base = alt.Chart(df)
    if group_choice == 'Gender':
        col1, col2 = st.columns(2)
        males = df[df['GENDER'] == 'Male']
        females = df[df['GENDER'] != 'Male']

        donutMale = alt.Chart(males).mark_arc(innerRadius=50, outerRadius=90).encode(
            theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
            color=alt.Color('Survival:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
            tooltip=['count(SUBJECT_ID)', 'Survival'],
        ).properties (
            title = 'Males'
        )

        donutFemale = alt.Chart(females).mark_arc(innerRadius=50, outerRadius=90).encode(
            theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
            color=alt.Color('Survival:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
            tooltip=['count(SUBJECT_ID)', 'Survival'],
        ).properties (
            title = 'Females'
        )

        with col1:
         st.altair_chart(donutMale)
        with col2:
         st.altair_chart(donutFemale)

    elif group_choice == 'Race':
        raceChart = alt.Chart(df).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', sort='-x', title="Number of patients"),
            y=alt.Y('Survival', axis=alt.Axis(labels=False, title=None)),
            color=alt.Color('Survival:N'),
            row= alt.Row('ETHNICITY', header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left')),
            tooltip=['count(SUBJECT_ID)', 'Survival'],
          ).properties(
            title=f"Ethnicity distribution",
            width=WIDTH
        )
        st.altair_chart(raceChart)

    elif group_choice == 'Age Group': 
        ageChart = alt.Chart(df).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', sort='-x', title="Number of patients"),
            y=alt.Y('Survival', axis=alt.Axis(labels=False, title=None)),
            color=alt.Color('Survival:N'),
            row= alt.Row('AGE_GROUP', header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left')),
            tooltip=['count(SUBJECT_ID)',  'Survival'],
          ).properties(
            title=f"Age distribution",
            width=WIDTH
        )
        st.altair_chart(ageChart)

    elif group_choice == 'Insurance': 
        insuranceChart = alt.Chart(df).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', sort='-x', title="Number of patients"),
            y=alt.Y('Survival', axis=alt.Axis(labels=False, title=None)),
            color=alt.Color('Survival:N'),
            row= alt.Row('INSURANCE', header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left')),
            tooltip=['count(SUBJECT_ID)',  'Survival'],
          ).properties(
            title=f"Insurance distribution",
            width=WIDTH

        )
        st.altair_chart(insuranceChart)

    elif group_choice == 'Religion': 
        rdf = df[df.RELIGION.notnull()]

        religionChart = alt.Chart(rdf).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', sort='-x',  title="Number of patients"),
            y=alt.Y('Survival', axis=alt.Axis(labels=False, title=None)),
            color=alt.Color('Survival:N'),
            #row = alt.Row('SHORT_TITLE', header=alt.Header(labelAngle=0))
            row= alt.Row('RELIGION', header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left')),
            tooltip=['count(SUBJECT_ID)',  'Survival'],
          ).properties(
            title=f"Religion distribution",
            width=WIDTH
        )
        st.altair_chart(religionChart)


    else:
        mdf = df[df.MARITAL_STATUS.notnull()]
        marriageChart = alt.Chart(mdf).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', sort='-x',  title="Number of patients"),
            y=alt.Y('Survival', axis=alt.Axis(labels=False, title=None)),
            color=alt.Color('Survival:N'),
            row= alt.Row('MARITAL_STATUS', header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left')),
            tooltip=['count(SUBJECT_ID)',  'Survival'],
          ).properties(
            title=f"Marital status distribution",
            width=WIDTH
        )

        st.altair_chart(marriageChart)

