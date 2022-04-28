import streamlit as st
import pandas as pd
import altair as alt



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

if death == 'all':
    subset = subset
else:
    subset = subset[subset["Death"] == death]

#domain = ('Expired', 'Survived')
#range_ = ['red', 'green']

chart = alt.Chart(subset).mark_rect().encode(
    x=alt.X('count(SUBJECT_ID)', title = 'number of patients'),
    y=alt.Y("SHORT_TITLE", title = 'Diagnosis'),
  
).properties(
    title=f"Number of Patients with Diagnosis",
    width=100,
    height=100,
)

st.altair_chart(chart)


