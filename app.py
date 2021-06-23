import streamlit as st
from predict_page import show_predict
from explore_page import show_explore

page = st.sidebar.selectbox("EXPLORE OR PREDICT",("PREDICT","EXPLORE"))
if page == "PREDICT":
    show_predict()
else:
    show_explore()
