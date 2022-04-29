import altair as alt
import streamlit as st
import pandas as pd

item = pd.read_csv('706/data/labItemFilter.csv')
lab_df = pd.read_csv('706/data/labPatientFilter.csv')

combined = lab_df.merge (item, on ='ITEMID', how = 'left')

st.write("## Abnormal Lab frequency")
lab_chosen_item = st.multiselect('choose lab',item.LABEL.unique(),
                                  default=['Polys','Monos','Macrophage'])
#lab_chosen_id = item.ITEMID[item.LABEL.isin(lab_chosen_item)]
#subset = lab_df[lab_df.ITEMID.isin(lab_chosen_id)]
#subset = df[df["SHORT_TITLE"].isin(options)]

subset = combined[combined["LABEL"].isin(lab_chosen_item)]

#st.dataframe(subset)
#st.dataframe(item[item.ITEMID.isin(lab_chosen_id)])
#st.write(f"Dataframe size:{subset.shape}")

death = st.radio(
    "select patients",
    ('Expired', 'Survived', 'All'))

if death == 'Expired':
    subset = subset[subset["EXPIRE_FLAG"] == 1]
elif death == 'Survived': 
    subset = subset[subset["EXPIRE_FLAG"] == 0]



barchart = alt.Chart(subset).mark_bar().encode(

    x=alt.X('count(SUBJECT_ID)', title = 'number of patients'),
    y=alt.Y("LABEL", title = 'lab'),

    #x = alt.X('ITEMID:N',title='ITEM'),
    #y = alt.Y('SUBJECT_ID',title='Patients'),
)
st.altair_chart(barchart,use_container_width=True)