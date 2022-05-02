import altair as alt
import streamlit as st
import pandas as pd


################# Lab barplot ######################
def app():
    item = pd.read_csv('706/data/labItemFilter.csv')
    lab_df = pd.read_csv('706/data/labPatientFilter.csv')
    lab_df['Death'] = lab_df['EXPIRE_FLAG'].map({0: 'Survived', 1: 'Expired'})

    # combined = lab_df.merge (item, on ='ITEMID', how = 'left')

    st.write("## Abnormal Lab frequency")

    # with st.sidebar:
    lab_chosen_item = st.multiselect('Choose lab',item.LABEL.unique(),
                                      default=['Red Blood Cells','RDW','pO2','Hemoglobin','Free Calcium','PTT'])

    st.markdown("""---""")

    subset_item = item[item['LABEL'].isin(lab_chosen_item)]
    subset = pd.merge(subset_item,lab_df,on='ITEMID',how='left')
    # subset = combined[combined["LABEL"].isin(lab_chosen_item)]
    # subset = combined

    barchart = alt.Chart(subset).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', title = 'number of patients'),
            y=alt.Y("Death:N",sort='-x', axis=alt.Axis(labels=False, title='lab conducted')),
            color = alt.Color("Death:N"),
            row = alt.Row('LABEL')
        ).properties(
            width=1000
        )
    st.altair_chart(barchart)
