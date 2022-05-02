
import streamlit as st
st.set_page_config(layout="wide")
# from multipage import MultiPage

import demographic_plot
import lab_barplot
import diag_barplot
import lab_time_scatter
import lab_value_demo
import home

PAGES = {
    "Home page": home,
    "Distrubition of demographics": demographic_plot,
    "Lab test distrubition": lab_barplot,
    "Diagnosis distrubition": diag_barplot,
    "Lab value Before ICU": lab_time_scatter,
    "Abnormal labs & demographics": lab_value_demo
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()