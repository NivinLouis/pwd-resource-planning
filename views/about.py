import streamlit as st
import time
import threading

st.header("This page will be updated soon", divider='grey')
def animate():
    with st.spinner('Wait for it...'):
        time.sleep(5)
     

t = threading.Thread(target=animate)
t.start()
animate()