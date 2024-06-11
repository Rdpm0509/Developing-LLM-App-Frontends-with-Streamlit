#SIDEBAR
import streamlit as st 

#side bar with a select box
my_select_box = st.sidebar.selectbox('Select', ['US', 'UK', 'DE', 'FR'])

#side bar with a slider
my_slider = st.sidebar.slider('Temperature')