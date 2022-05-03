import altair as alt
import streamlit as st
import pandas as pd


################# Lab barplot ######################
def app():
    item = pd.read_csv('706/data/labItemFilter.csv')
    lab_df = pd.read_csv('706/data/labPatientFilter.csv')
    lab_df['Survival'] = lab_df['EXPIRE_FLAG'].map({0: 'Survived', 1: 'Expired'})

    # combined = lab_df.merge (item, on ='ITEMID', how = 'left')

    st.write("## Abnormal Lab frequency")
    st.write("If you'd like to compare the survival status frequency distribution of a few different lab tests, use this visualization page. We also have a page for visualizing diagnoses. We separated them in consideration of the computation time.")
    st.write("The results can get a little delayed because we are querying from a record with around 3.2 million conducted lab tests.")
    # with st.sidebar:
    lab_chosen_item = st.multiselect('Add lab tests of interest',item.LABEL.unique(),
                                      default=['Red Blood Cells','RDW','pO2','Hemoglobin','Free Calcium','PTT'])

    st.markdown("""---""")

    subset_item = item[item['LABEL'].isin(lab_chosen_item)]
    subset = pd.merge(subset_item,lab_df,on='ITEMID',how='left')
    # subset = combined[combined["LABEL"].isin(lab_chosen_item)]
    # subset = combined

    barchart = alt.Chart(subset).mark_bar().encode(
            x=alt.X('count(SUBJECT_ID)', title = 'Number of records'),
            y=alt.Y("Survival:N",sort='-x', title = 'Lab tests', axis=alt.Axis(labels=False, title = '')),
            color = alt.Color("Survival:N"),
            row = alt.Row('LABEL', title = 'Lab tests'),
            tooltip=['count(SUBJECT_ID)',  'Survival'],
        ).properties(
            width=800
        )
    st.altair_chart(barchart)
