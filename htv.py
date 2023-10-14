import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Investment Rec Engine", page_icon="📈", layout="wide")
st.title('Investment Rec Engine')
with st.sidebar:
    st.header('How to use our app')
    st.write("""
Input your deomgraphic and financial information into the website. Click on 
'Generate' to create recommendations for indices, stocks and bonds that you may
profit from investing in.

Important Note: We do not guarantee that any suggestions given will definitely 
result in profit. Our app just provides suggestions as to where you may start 
your research into which options may be profitable. The market is volatile and 
profitability cannot be determined with complete certainty.

Disclaimer: Your data will remain anonymous and will stay within our app. Your
data may be used to expand our dataset so that we can make even more accurate
predictions in the future.
""")

age = st.slider('Select your age', 0, 100, 25)
if st.button('Submit'):
    st.success(f"You selected age: {age}")


text = st.text_input('Enter your Income:', '')

option = st.selectbox('Select your Income Group', ['<$40k', '$40k - $70k', '$70k - $100k', '$100k - $150k', '>$150k'])

option = st.selectbox('Select your Asset Value', ['<$40k', '$40k - $70k', '$70k - $100k', '$100k - $150k', '>$150k'])

option = st.selectbox('Select your Debt', ['$0k', '<$20k','<$50k', '<$100k'])

option = st.selectbox('Select your Risk Tolerance', ['<$40k', '40k - 70k', '70k - 100k', '100k - 150k', '>150k'])

text = st.text_input('Enter your Assets:', '')
text = st.text_input('Enter your Debt:', '')
text = st.text_input('Enter your Risk Tolerance:', '')

st.write(f'Output:')

@st.cache_data
def expensive_computation():
    # Run the model for a given input
    return 0

result = expensive_computation()
st.write(result)


option = st.selectbox('Select an option', ['Option 1', 'Option 2'])
st.write(f'You selected: {option}')

if option == 'Option 1':
    st.info('You chose Option 1.')
elif option == 'Option 2':
    st.info('You chose Option 2.')

