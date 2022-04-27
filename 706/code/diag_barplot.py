import streamlit as st
import pandas as pd
import altair as alt



df = pd.read_csv("706/data/diags.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

st.write('hello world!')
chart = alt.Chart(df).mark_rect().encode(
    x=alt.X("ICD9_CODE"),
    y='count(SUBJECT_ID)',
    
).properties(
    #title=f"{cancer} mortality rates for {'males' if sex == 'M' else 'females'} in {year}",
)


