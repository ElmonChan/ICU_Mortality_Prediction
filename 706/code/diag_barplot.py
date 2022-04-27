import streamlit as st
import pandas as pd
import altair as alt



df = pd.read_csv("706/data/diags_new.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

def label_death (row):
   if row['EXPIRE_FLAG'] == 1 :
      return 'Expired'
   return 'Survived'

df['Death'] = df.apply (lambda row: label_death(row), axis=1)

icd9_codes = [
    "4019",
    "4280",
    "2724",
]

options = st.multiselect(
     'ICD9 Code',
     df["ICD9_CODE"].unique(),
     icd9_codes)
subset = df[df["ICD9_CODE"].isin(icd9_codes)]


death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'all'))

if death == 'all':
    subset = subset
else:
    subset = subset[subset["Death"] == death]



chart = alt.Chart(subset).mark_rect().encode(
    x=alt.X("ICD9_CODE"),
    y=alt.Y('count(SUBJECT_ID)', title = 'number of patients'),
    color = alt.Color('Death'),
  
).properties(
    title=f"ICD_Code",
)

st.altair_chart(chart)


