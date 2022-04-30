import altair as alt
import streamlit as st
import pandas as pd

st.write('Hello world!')

icu_labs = pd.read_csv('706/data/icu_lab.csv')