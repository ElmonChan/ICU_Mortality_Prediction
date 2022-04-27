import streamlit as st
import pandas as pd
import altair as alt



df = pd.read_csv("706/data/diags.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

def label_death (row):
   if row['EXPIRE_FLAG'] == 1 :
      return 'Expired'
   return 'Survived'

df['Death'] = df.apply (lambda row: label_death(row), axis=1)


death = st.radio(
    "Death",
    ('Expired', 'Survived'))

subset = df[df["Death"] == death]



chart = alt.Chart(subset).mark_rect().encode(
    x=alt.X("ICD9_CODE"),
    y=alt.Y('count(SUBJECT_ID)', title = 'number of patients'),
    
).properties(
    title=f"ICD_Code",
)

st.altair_chart(chart)


