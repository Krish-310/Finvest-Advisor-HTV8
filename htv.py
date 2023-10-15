import streamlit as st
import pandas as pd
import numpy as np
import os
import logging
from dotenv import load_dotenv
import cohere
import torch
import random
from random import gauss

# Logging
logging.getLogger("complete").setLevel(logging.WARNING)

# Load env variables
load_dotenv()
# Note: Cohere API key is no longer part of this project for now

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

# Getting input from the user

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
st.write("""
Note: Risk Tolerance refers to the risk that you are willing to take when you make your investment.
A lower risk typically implies lower returns, whereas a higher risk has the chance to yield higher returns.
""")

st.markdown("\n")

def on_button_click():
    st.write("Submission Complete!")

button_clicked = st.button("Generate")

if button_clicked:
    on_button_click()

st.write("\n")

# End of input from user

# Processing User Input

def vector_length(vector):
    length = np.linalg.norm(vector)
    return length
def person_data():
    user_data = [age, income, asset, debt, credit_score, risk]
    return user_data

def nested_array_converted():
    # Load your CSV file, replace 'your_data.csv' with the actual file path
    df = pd.read_csv('your_data.csv')
    # Extract the data columns (excluding the name column)
    data_columns = df.columns[1:]  # The first column is the name
    # Create a list of lists for each person's data
    person_data_list = []
    for _, row in df.iterrows():
        person_data = row[data_columns].tolist()
        person_data_list.append(person_data)
    personal_data_list_np = np.array(personal_data_list)
    return personal_data_list_np


def dot_product():
    a = nested_array_converted()
    dot = []
    b = personal_data() # numpy list
    for i in range(a.shape[0]): # Number of rows in the 2D array
        p = a[i] @ b
        dot.append(p)
    dot_np = np.array(dot)
    return dot_np


def cosine():
    dot = dot_product() # numpy list
    cos = []
    len_b = vector_length(person_data()) # number
    nested = nested_array_converted() # numpy list
    for i in dot.size():
        len_a =  vector_length(nested[i])
        cos_theta = dot[i]/(len_b * len_a)
        cos.append(cos_theta)
    cos_np = np.array(cos)
    return cos_np


# Now, we find the max in the cos array:
def max_cosine():
    cosine_array = cosine()
    return cosine_array.max()



# Set a random seed for reproducibility
random.seed(0)
torch.manual_seed(0)

# Create empty lists to store the data
people_data = []

# Generate data for 100 people
for _ in range(100):
    income = random.randint(30000, 200000)  # Income between $30,000 and $120,000\
    income_num=0
    if income <40000:
      income_num =1
    elif income< 53359:
      income_num=2
    elif income <106717:
      income_num=3
    elif income <165430:
      income_num = 4
    elif income <235675:
      income_num =5
    else:
      income_num =6
    credit_score = random.randint(300, 900)  # Credit score between 400 and 850
    asset_value = random.uniform(10000, 500000)  # Asset value between $10,000 and $500,000
    debt_value = random.uniform(0, asset_value)  # Debt value is less than or equal to asset value
    risk_tolerance = random.choice([1,1.5,2,2.5,3])  # Risk tolerance level (1, 2, 3)

 
    # Create a dictionary representing a person's data
    person = {
        "Income Score": income_num,
        "Credit Score": credit_score,
        "Asset Value": asset_value,
        "Debt Value": debt_value,
        "Risk Tolerance": risk_tolerance
    }

    people_data.append(person)

 
# Apply transformations to income, asset value, and debt value

# making pandas file
people_df = pd.DataFrame(people_data)
people_df['ID'] = range(1, len(people_df) + 1)
people_df.head(100)
pd.set_option('display.max_rows', None)

# Display the first few records

# for i in range(100):

#     print(f"Person {i + 1}: {people_data[i]}")

 

# You can access the data for each person using people_data[index]

# For example, to access the risk tolerance score of the first person:

# risk_tolerance_of_first_person = people_data[0]["Risk Tolerance"]

# people_df

fund_data = pd.read_csv(r'/content/sample_data/HV_8_Fund_Data.csv')

fund_data['hash values'] = range(1, len(fund_data) + 1)

# fund_data


# Convert the DataFrame to a string

fund_data_string = fund_data.to_string(index=False, header=False)

 

# Display the resulting string

# print(fund_data_string)

people_df_string = people_df.to_string(index=False, header=False)

# people_df_string

# !pip install cohere

 

import cohere

co = cohere.Client(API_KEY)

text = people_df_string

lines = text.splitlines()

var_data= range(1, 100)

 

import random 

data_mapped = []


for i in range(100):
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    z = random.randint(1, 50)

    # Create a dictionary for the new row
    new_row = {
        'Person_ID': i,
        'Priority 1': x,
        'Priority 2': y,
        'Priority 3': z
    }

    # Append the new row to the list

    data_mapped.append(new_row)

 

# Create a DataFrame from the list of dictionaries

data_mapped_df = pd.DataFrame(data_mapped)

 

# Print the DataFrame to see the result

# print(data_mapped_df)

 

# # Display each line

# # for line in lines:

#     # print(line)

# response = co.generate(

#   prompt = " Suppose you are a pesron having Income-Score          Credit-Score Asset-Value Debt-Value Risk-Tolerance ID as " + line + " respectively, provide me three row numbers of the assets  in terms of priority from " + fund_data_string + " in which you are likely to invest in"

#       # prompt= "using the"+people_df_string+"build me another dataset where each value in"+people_df_string +"rates each value of"+fund_data_string+"based on how likely each person in"+people_df_string+"to buy the given investment option in"+fund_data_string+"the ratings should be from 1-5 where 1 is least likely to buy and 5 is most likely to buy"

# )

# print(response[0])






# Producing Output for the user 

st.header(f'Potential Recommendations to Invest in:')


if button_clicked:
    st.write("information")

result = """
US Dollar Index Futures - Dec 23 (DXZ3) ---- https://ca.investing.com/currencies/us-dollar-index \n
Tesla Inc (TSLA) ---- https://ca.investing.com/equities/tesla-motors \n
United States 2-Year Bond Yield ---- https://ca.investing.com/rates-bonds/u.s.-2-year-bond-yield \n
"""


st.write(result)

