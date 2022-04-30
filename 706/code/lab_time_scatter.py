import altair as alt
import streamlit as st
import pandas as pd

st.write('Hello world!')

icu_labs = pd.read_csv('706/data/icu_lab.csv')

options = st.selectbox(
     'select lab',
     icu_labs.LABEL.unique())

subset = icu_labs[icu_labs["LABEL"].isin(options)]

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    subset = subset[subset["EXPIRE_FLAG"] == 1]
elif death == 'Survived': 
    subset = subset[subset["EXPIRE_FLAG"] == 0]
