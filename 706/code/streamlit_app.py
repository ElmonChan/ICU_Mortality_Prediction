
import streamlit as st
st.set_page_config(layout="wide")
# from multipage import MultiPage

import demographic_plot
import lab_barplot
import diag_barplot
import lab_time_scatter

PAGES = {
    "Demographic": demographic_plot,
    "Lab": lab_barplot,
    "Diagnosis": diag_barplot,
    "Lab Value Before ICU": lab_time_scatter
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()