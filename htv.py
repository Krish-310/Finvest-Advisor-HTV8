import streamlit as st
import pandas as pd
import numpy as np

# Front-End of the Web App with Streamlit

st.set_page_config(page_title="Investment Recommendation Engine", page_icon="📈", layout="wide")

st.title('Investment Recommendation Engine')
with st.sidebar:
    st.header('How to use our app')
    st.write("""
Input your deomgraphic and financial information into the site and click on 
'Generate' to create recommendations for indices, stocks and bonds that you may
profit from investing in.

Important Note: We do not guarantee that these recommendations ascertain profit. 
Our app provides suggestions as to where you may start 
your research into options that may be profitable. The market is volatile and 
profitability cannot be determined with complete certainty.

Disclaimer: Your data will remain anonymous and will stay within our app. Your
data may be used to expand our dataset so that we can make even more accurate
predictions in the future.
""")

st.markdown("This is a Machine Learning model which gets trained on the data that it gets. Do not be completely reliant on the results it provides.")

# Getting input from the user as data

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

risk = st.selectbox('Select your Risk Tolerance', ['Low', 'Low to Medium', 'Medium', 'Medium to High', 'High'])
st.write("""
Note: Risk Tolerance refers to the risk that you are willing to take when you make your investment.
A lower risk typically implies lower returns, whereas a higher risk has the chance to yield higher returns.
""")

st.markdown("\n")


button_clicked = st.button("Generate")


st.markdown("\n")
st.write("\n")

# End of input from user


# Processing User Input (Backend Side of the project)

if income == '< $53,359':
    user_income_num = 2
elif income == '$53,359 - $106,717':
    user_income_num = 3
elif income == '$106,717 - $165,430':
    user_income_num = 4
elif income == '$165,430 - $235,675':
    user_income_num = 5
else:
    user_income_num = 6

if risk == 'Low':
    risk_num = 1
elif risk == 'Low to Medium':
    risk_num = 1.5
elif risk == 'Medium':
    risk_num = 2
elif risk == 'Medium to High':
    risk_num = 2.5
elif risk == 'High':
    risk_num = 3

if asset == '<$100k':
    asset_num = 100000
elif asset == '<$200k':
    asset_num = 200000
elif asset == '<$400k':
    asset_num = 400000
elif asset == '<$600k':
    asset_num = 600000
elif asset == '<$800k':
    asset_num = 800000
elif asset == '<$1M':
    asset_num = 1000000
elif asset == '>$1M':
    asset_num = 1100000

if debt == '$0k':
    debt_num = 0
elif debt == '<$20k':
    debt_num = 20000
elif debt == '<$50k':
    debt_num = 50000
elif debt == '<$100k':
    debt_num = 100000
elif debt == '<$200k':
    debt_num = 200000
elif debt == '>$200k':
    debt_num = 210000

def vector_length(vector):
    length = np.linalg.norm(vector)
    return length
def person_data():
    user_data = [age, user_income_num, credit_score, asset_num, debt_num, risk_num]
    user_data_np = np.array(user_data)
    return user_data_np

def nested_array_converted():
    # Load your CSV file, replace 'your_data.csv' with the actual file path
    df = pd.read_csv('person_data.csv')
    # Extract the data columns (excluding the name column)
    data_columns = df.columns[0:6]  # The first column is the name
    # Create a list of lists for each person's data
    person_data_list = []
    for _, row in df.iterrows():
        person_data = row[data_columns].tolist()
        person_data_list.append(person_data)
    personal_data_list_np = np.array(person_data_list)
    return personal_data_list_np


def dot_product():
    a = nested_array_converted()
    dot = []
    b = person_data() # numpy list
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
    for i in range(dot.size):
        len_a =  vector_length(nested[i])
        cos_theta = dot[i]/(len_b * len_a)
        cos.append(cos_theta)
    cos_np = np.array(cos)
    return cos_np


# Now, we find the max in the cos array:
def max_cosine():
    cosine_array = cosine()
    a = cosine_array.max()
    for i in range(cosine_array.size):
        if cosine_array[i] == a:
            return i

def get_person_choice():
      df = pd.read_csv('data_mapped.csv')
      numpy_array = df.to_numpy()
      index= max_cosine()
      df_data= numpy_array[index][1:]
      return df_data
    
def front_end_return():
    df = pd.read_csv('Funds.csv')
    na = df.to_numpy()
    index_list = get_person_choice()
    print(index_list[0], index_list[1], index_list[2])
    a = [[na[index_list[0]][0], na[index_list[0]][4] ],
         [na[index_list[1]][0], na[index_list[1]][4] ],
         [na[index_list[2]][0], na[index_list[2]][4] ]]
    return a

# End of Backend for the project


# Front-End: Producing Output for the user 

st.header(f'Potential Recommendations to Invest in:')

st.markdown("\n")

if button_clicked:
    investments = front_end_return()
    st.write("\n")
    st.write(investments[0][0] + " ---- " + investments[0][1])
    st.write(investments[1][0] + " ---- " + investments[1][1])
    st.write(investments[2][0] + " ---- " + investments[2][1])
else:
    st.write("\n")
    st.write("Fill in your data first and then click generate!")


