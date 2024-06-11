# this code is useful in case you run a lot of applications. 
# it keeps track of the processes and tell you if the code got stuck or into any errors
import streamlit as st
import time 
st.write('Starting an extensive computation ...')
latest_iteration = st.empty() #container that holds an element

progress_text = 'Operation in progress. Please wait ...'
my_bar = st.progress(0, text=progress_text) # messageg to display above the proress bar
time.sleep(2)

for i in range(100):
    my_bar.progress(i+1)
    latest_iteration.text(f'Iteration {i+1}')
    time.sleep(0.1) #faking a timespan

st.write('We are done! :+1:')