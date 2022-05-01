import streamlit as st
import pandas as pd
import altair as alt

def app():
    st.write("## Diagnosis frequency")

    df = pd.read_csv("706/data/diags_new.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

    def label_death (row):
       if row['EXPIRE_FLAG'] == 1 :
          return 'Expired'
       return 'Survived'

    df['Death'] = df.apply (lambda row: label_death(row), axis=1)


    short_titles = [
        "Hypertension NOS",
        "Depressive disorder NEC",
    ]

    options = st.multiselect(
         'select diagnosis',
         df["SHORT_TITLE"].unique(),
         short_titles)
    subset = df[df["SHORT_TITLE"].isin(options)]


    death = st.radio(
        "select patients",
        ('Expired', 'Survived', 'All'))

    if death == 'Expired':
        subset = subset[subset["EXPIRE_FLAG"] == 1]
    elif death == 'Survived':
        subset = subset[subset["EXPIRE_FLAG"] == 0]


    #domain = ('Expired', 'Survived')
    #range_ = ['red', 'green']

    chart = alt.Chart(subset).mark_rect().encode(
        x=alt.X('count(SUBJECT_ID)', title = 'number of patients'),
        y=alt.Y("SHORT_TITLE", title = 'Diagnosis'),
        #color = ('Death')

    ).properties(
        #title=f"Number of Patients with Diagnosis",
        width=800,
    )

    st.altair_chart(chart, use_container_width=True)


