import streamlit as st 
import pandas as pd 

# Displaying data on the screen: 

st.title('Hello Streamlit World! :100:')

# 1. st.write()

st.write('We learn how to write on the screen using st.write()')
l1 = [1,2,3]
st.write(l1)

l2 = list('abc')
d1 = dict(zip(l1,l2))
st.write(d1)

# 2. Magic
'Displaying using magic :smile:'

df = pd.DataFrame({
    'first_column':[1,2,3,4],
    'second_column':[10,20,30,40]
})

df # this is the same as st.write(df)