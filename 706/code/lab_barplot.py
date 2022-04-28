import altair as alt
import streamlit as st
import pandas as pd

item = pd.read_csv('706/data/labItemFilter.csv')
lab_df = pd.read_csv('706/data/labPatientFilter.csv')


st.write("## Abnormal Lab frequency")
lab_chosen_item = st.multiselect('Lab',item.LABEL.unique(),
                                  default=['Polys','Monos','Macrophage'])
lab_chosen_id = item.ITEMID[item.LABEL.isin(lab_chosen_item)]
subset = lab_df[lab_df.ITEMID.isin(lab_chosen_id)]

st.dataframe(subset)
st.dataframe(item[item.ITEMID.isin(lab_chosen_id)])
st.write(f"Dataframe size:{subset.shape}")

barchart = alt.Chart(subset).mark_bar().encode(
    x = alt.X('ITEMID:N',title='ITEM'),
    y = alt.Y('SUBJECT_ID',title='Patients'),
)
st.altair_chart(barchart,use_container_width=True)