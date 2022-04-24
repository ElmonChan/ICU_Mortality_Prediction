import streamlit as st
import pandas as pd


df = pd.read_csv("/706/data/diags.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

st.write('hello world!')

