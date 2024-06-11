import streamlit as st 
import pandas as pd

# PS: you should always treat your widges as variables

# Text input 
name = st.text_input('Your name: ')
if name:
    st.write(f'Hello {name}')

# Number input
x = st.number_input('Enter a number', min_value=1, max_value=99, step=1)
st.write(f'The current number is {x}')

# Horizontal line for a better readability
st.divider()

# Button
clicked = st.button('Click me!')
if clicked: 
    st.write(':ghost: * 3')

# Horizontal line for a better readability
st.divider()    

# CHECKBOX (returns True if the user click the box)
agree = st.checkbox('I agree')
if agree: 
    'Great, you agreed!'

# True value as a default
checked = st.checkbox('Continue', value=True)
if checked:
    ':+1: '* 5

df = pd.DataFrame({
    'Name': ['Anne', 'Mario', 'Douglas'],
    'Age': [30,25,40]
})

if st.checkbox('Show data'):
    st.write(df)

st.divider()
# RADIO
pets = {'cat', 'dog', 'fish', 'turtle'}
pet = st.radio('Favorite pet', pets) #index=0)#it means the selection starts at 'cat'
st.write(f'Your favorite pet: {pet}')

st.divider()
# Select option
cities = ['SP', 'MG', 'RJ', 'PE']
city = st.selectbox('Your city', cities)
st.write(f'You live in {city}')