import altair as alt
import streamlit as st

def app():
    st.write("## Study of patient information with cardiovascular diseases")
    st.write("##### Feng Chen, Elmon Chen, Richard Yang, Ning Hua")
    st.write("##### Spring 2022 @Harvard Medical School")
    st.write("Heart failure (HF) has been a major clinical and public health problem since its designation as a new epidemic in 1997 (Braunwald, 1997). Despite enormous efforts by public health organizations to treat and control HF, studies show that the burden of death and hospitalization remains mostly unchanged (Levy et al., 2002; Roger et al., 2004). In the CDC's 1999-2020 summary of underlying causes of death in the United States, heart failure still ranks first (Centers for Disease Control and Prevention, 2022).")
    st.write("At the same time, the digitalization of medical and clinical information has made a major contribution to the study of diseases (Kraus et al., 2021). Here, we use data collected and extracted from a large de-identified publicly available dataset called MIMIC III to build a visualization tool for easier investigation of the information of patients with cardiovascular diseases. We majorly focus on ***lab tests*** and ***patient demographics***.")
    st.markdown("[MIMIC III](https://physionet.org/content/mimiciii-demo/1.4/) (Johnson et al., 2016) contains de-identified health-related data for over 38,597 patients who stayed in the Beth Israel Deaconess Medical Center's intensive care unit between 2001 and 2012. Demographics, vital sign measurements taken at the bedside, laboratory test results, procedures, prescriptions, carer notes, imaging reports, and mortality are all included in the database.")
    st.markdown("""----""")
    st.markdown("##### Reference")
    st.write("""Alsentzer, E., Murphy, J. R., Boag, W., Weng, W.-H., Jin, D., Naumann, T., & McDermott, M. B. A. (2019). Publicly Available Clinical BERT Embeddings. ArXiv:1904.03323 [Cs]. http://arxiv.org/abs/1904.03323
                \nBraunwald, E. (1997). Cardiovascular Medicine at the Turn of the Millennium: Triumphs, Concerns, and Opportunities. New England Journal of Medicine, 337(19), 1360–1369. https://doi.org/10.1056/NEJM199711063371906
                \nCasey, J. A., Schwartz, B. S., Stewart, W. F., & Adler, N. E. (2016). Using Electronic Health Records for Population Health Research: A Review of Methods and Applications. Annual Review of Public Health, 37(1), 61–81. https://doi.org/10.1146/annurev-publhealth-032315-021353
                \nCowieCenters for Disease Control and Prevention. (2022, January 5). Underlying Cause of Death 1999-2020 on CDC WONDER Online Database, released in 2021. https://wonder.cdc.gov/controller/datarequest/D76;jsessionid=F8FDEDBB6161B3077A10B536D933
                \nDar, O., & Cowie, M. R. (2008). Acute heart failure in the intensive care unit: Epidemiology. Critical Care Medicine, 36(1 Suppl), S3-8. https://doi.org/10.1097/01.CCM.0000296264.41365.80
                \nJohnson, A. E. W., Pollard, T. J., Shen, L., Lehman, L. H., Feng, M., Ghassemi, M., Moody, B., Szolovits, P., Anthony Celi, L., & Mark, R. G. (2016). MIMIC-III, a freely accessible critical care database. Scientific Data, 3(1), 160035. https://doi.org/10.1038/sdata.2016.35
                \nKraus, S., Schiavone, F., Pluzhnikova, A., & Invernizzi, A. C. (2021). Digital transformation in healthcare: Analyzing the current state-of-research. Journal of Business Research, 123, 557–567. https://doi.org/10.1016/j.jbusres.2020.10.030""")