import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

lottie_welcome= load_lottiefile("assets\welcome.json")

st.set_page_config(page_title="Welcome",layout="wide")

col1, col2 = st.columns([1,1])

with col1:
    #st.markdown("You are logged in to")
    st.title('')
    st.title('Care Connect')
    st.header('')
    st.markdown("Designed with a mission to aid in the collection and analysis of data concerning disabled individuals, aims to bridge the gap between data accessibility and meaningful insights. Provides user-friendly interfaces to streamline the process of gathering and interpreting crucial information.The software aims to support informed decision-making for the greater good.")
with col2:
    st_lottie(
        lottie_welcome,
        speed=1,
        loop=True,
        quality="low",
        #renderer="svg",
        height=None,
        width=None,
    )