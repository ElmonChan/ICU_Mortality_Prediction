import streamlit as st
import pandas as pd
import altair as alt

def app():
    st.write("## Diagnosis frequency")
    st.write("This page allows exploration of diagnoses and survival status.")

    st.markdown("""---""")

    df = pd.read_csv("706/data/diags_new.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

    def label_death (row):
       if row['EXPIRE_FLAG'] == 1 :
          return 'Expired'
       return 'Survived'

    df['Survival'] = df.apply (lambda row: label_death(row), axis=1)



    #totalSurvived = len(df.loc[df.Survival.eq('Survived')])
    #totalExpired = len(df.loc[df.Survival.eq('Expired')])



    short_titles = [
        "Hypertension NOS",
        "Depressive disorder NEC",
        "Acute respiratry failure",
        "Pneumonia, organism NOS", 
        "History of tobacco use",
        "Tobacco use disorder"
    ]

    options = st.multiselect(
         'Add diagnoses of interest',
         df["SHORT_TITLE"].unique(),
         short_titles)
    subset = df[df["SHORT_TITLE"].isin(options)]


    chart = alt.Chart(subset).mark_rect().encode(
        x=alt.X('count(SUBJECT_ID)', title = 'Number of records'),
        #y=alt.Y("SHORT_TITLE", title = 'Diagnosis'),
        y=alt.Y("Survival:N",sort='-x', title = 'Diagnoses', axis=alt.Axis(labels=False, title='')),
        color = alt.Color("Survival:N"),
        tooltip=['count(SUBJECT_ID)',  'Survival'],
        row = alt.Row('SHORT_TITLE', title="Diagnosis distrubition", header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left'))

    ).properties(
        #title=f"Number of Patients with Diagnosis",
        width=800,
    )

    chart1 = alt.Chart(subset).transform_joinaggregate (
        totalPeoople = subset.shape[0],
    ).transform_calculate (
        percents = 'datum.count(SUBJECT_ID) / datum.totalPeople'
    ).mark_rect().encode(
        x=alt.X('percents', title = 'percentage'),
        #y=alt.Y("SHORT_TITLE", title = 'Diagnosis'),
        y=alt.Y("Survival:N",sort='-x', title = 'Diagnoses', axis=alt.Axis(labels=False, title='')),
        color = alt.Color("Survival:N"),
        tooltip=['count(SUBJECT_ID)',  'Survival'],
        row = alt.Row('SHORT_TITLE', title="Diagnosis distrubition", header=alt.Header(labelAngle=0, labelAlign='left', titleOrient='top', labelOrient='left'))

    ).properties(
        #title=f"Number of Patients with Diagnosis",
        width=800,
    )


    st.altair_chart(chart1,)


