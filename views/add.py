import streamlit as st

st.title("Add Records")
col1, col2,col3 = st.columns([4,2,4])

with col1:
    st.subheader("")
    st.subheader("Scan the given QR code to visit the form")
    st.subheader("")
    st.markdown("Only adding through google forms is supported as of now. The excel file consisting of resposnses must be downloaded and uploaded in the Import tab")
    
with col3:
    st.image(image="assets\qframe.png", caption=None, width=256, use_column_width=None)