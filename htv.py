import streamlit as st
import pandas as pd
import numpy as np
import os
import logging
from dotenv import load_dotenv
import cohere

# Logging
logging.getLogger("complete").setLevel(logging.WARNING)
# Load env variables
load_dotenv()

#co = cohere.Client(os.getenv("COHERE_API_KEY"))




st.set_page_config(page_title="Investment Recommendation Engine", page_icon="📈", layout="wide")
st.title('Investment Recommendation Engine')
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

st.markdown("\n")

st.header(f'Please input your data as follows:')

age = st.slider('Select your age', 0, 100, 25)

st.write("\n")

income = st.selectbox('Select your Income Group', ['< $53,359', '$53,359 - $106,717', '$106,717 - $165,430', '$165,430 - $235,675', '> $235,675'])

asset = st.selectbox('Select your Asset Value', ['<$100k', '<$200k', '<$400k', '<$600k', '<$800k', '<$1M', '>$1M'])

debt = st.selectbox('Select your Approximate Debt', ['$0k', '<$20k','<$50k', '<$100k', '<$200k', '>$200k'])

st.write("\n")

credit_score = st.slider('What is your credit score', 300, 850, 700)

st.write("\n")

risk = st.selectbox('Select your Risk Tolerance', ['Low', 'Low to Medium', 'Medium', 'Medium to High'])
st.write("Note: ")

st.markdown("\n")

def on_button_click():
    st.write("Submission Complete!")

button_clicked = st.button("Generate")

if button_clicked:
    on_button_click()

st.write("\n")

st.header(f'Potential Recommendations to Invest in:')


# Feed data into model and return 3 investment options from the database

if button_clicked:
    st.write("information")

result = """
US Dollar Index Futures - Dec 23 (DXZ3) ---- https://ca.investing.com/currencies/us-dollar-index \n
Tesla Inc (TSLA) ---- https://ca.investing.com/equities/tesla-motors \n
United States 2-Year Bond Yield ---- https://ca.investing.com/rates-bonds/u.s.-2-year-bond-yield \n
"""


st.write(result)

