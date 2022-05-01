#from tkinter.tix import COLUMN
import pandas as pd
import altair as alt
import streamlit as st
import numpy as np

def app():

    st.write("## Demographic profile")

    group_choice = st.radio(
        "Group By",
        ('Gender', 'Race', 'None')
    )
    st.markdown("""---""")

    col1, col2, col3 = st.columns(3)

    ################# Demographic ######################
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
    df['Death'] = df['EXPIRE_FLAG'].map({0: 'Survived', 1: 'Expired'})

    # with st.sidebar:

    base = alt.Chart(df)

    if group_choice == 'Gender':
        # bar1 = base.mark_bar().encode(
        #     y = alt.Y('count(SUBJECT_ID)'),
        #     x = alt.X('GENDER',axis=alt.Axis( labels=False,title='')),
        #     color = alt.Color('GENDER:N',scale=alt.Scale(range=['#EA98D2', '#659CCA']),legend=None),
        #     column = 'AGE_GROUP',
        #     tooltip = ['count(SUBJECT_ID)','AGE_GROUP','GENDER:N'],
        #     #column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
        #     )

        # bar2 = base.mark_bar().encode(
        #     y=alt.Y('ETHNICITY:N', sort='-x'),
        #     x=alt.X('count(SUBJECT_ID)'),
        #     color=alt.Color('GENDER:N',scale=alt.Scale(range=['#EA98D2', '#659CCA']),legend=None),
        #     row=alt.Row('GENDER',title='',spacing=5,header=alt.Header(labels=False)),
        #     tooltip=['count(SUBJECT_ID)', 'ETHNICITY', 'GENDER:N'],
        # )

        males = df[df['GENDER'] == 'Male']
        females = df[df['GENDER'] != 'Male']

        donutMale = alt.Chart(males).mark_arc(innerRadius=50, outerRadius=90).encode(
            theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
            color=alt.Color('Death:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
            tooltip=['count(SUBJECT_ID)', 'Death'],
        ).properties (
            title = 'Males'
        )

        donutFemale = alt.Chart(females).mark_arc(innerRadius=50, outerRadius=90).encode(
            theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
            color=alt.Color('Death:N',scale=alt.Scale(range=['#EA98D2', '#659CCA'])),
            tooltip=['count(SUBJECT_ID)', 'Death'],
        ).properties (
            title = 'Females'
        )

        with col1:
         st.altair_chart(donutMale)
        with col2:
         st.altair_chart(donutFemale)



    elif group_choice == 'Race':
        # bar1 = base.mark_bar().encode(
        #     y=alt.Y('count(SUBJECT_ID)'),
        #     x=alt.X('Death', axis=alt.Axis(labels=False, title='')),
        #     color=alt.Color('Death', legend=None),
        #     column='AGE_GROUP',
        #     tooltip=['count(SUBJECT_ID)', 'AGE_GROUP', 'Death'],
        #     # column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
        # )


        # bar2 = base.mark_bar().encode(
        #     y=alt.Y('ETHNICITY:N', sort='-x'),
        #     x=alt.X('count(SUBJECT_ID)'),
        #     color=alt.Color('Death', legend=None),
        #     row=alt.Row('Death', title='', spacing=5, header=alt.Header(labels=False)),
        #     tooltip=['count(SUBJECT_ID)', 'ETHNICITY', 'Death'],
        #     # row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
        # )

        # donut = base.mark_arc(innerRadius=50, outerRadius=90).encode(
        #     theta=alt.Theta(aggregate="count", field='SUBJECT_ID', type='quantitative'),
        #     color=alt.Color(field='Death'),
        #     tooltip=['count(SUBJECT_ID)', 'Death']
        # )

        raceChart = alt.Chart(df).mark_bar().encode(
            x=alt.X("Death:N",sort='-x', axis=alt.Axis(labels=False, title='')),
            y=alt.Y('count(SUBJECT_ID)', title = 'number of patients'),

            color = alt.Color("Death:N"),
            column = alt.Column('ETHNICITY')
        ).properties(
            width=200
        )
        st.altair_chart(raceChart)


    else:

        bar1 = base.mark_bar().encode(
            y=alt.Y('count(SUBJECT_ID)'),
            x=alt.X('AGE_GROUP'),
            tooltip=['count(SUBJECT_ID)', 'AGE_GROUP'],
            # column = alt.Column('AGE_GROUP', header = alt.Header(labelOrient = "bottom"))
        ).properties(
            width=500
        )

        bar2 = base.mark_bar().encode(
            y=alt.Y('ETHNICITY', sort='-x'),
            x=alt.X('count(SUBJECT_ID)'),
            tooltip=['count(SUBJECT_ID)', 'ETHNICITY'],
            # row = alt.Row('ETHNICITY', header = alt.Header(labelOrient = "bottom"))
        ).properties(
            width=500
        )


    # with col1:
    #     st.altair_chart(bar1)
    # with col2:
    #     st.altair_chart(bar2)

    # if group_choice != 'None':
    #     donut = donut.properties(
    #             title="Proportion of expired patients in gender",
    #             width=400
    #         )
    #     with col3:
    #         st.altair_chart(donut)
