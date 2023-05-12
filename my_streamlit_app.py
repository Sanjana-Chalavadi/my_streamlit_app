# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col,lit
import streamlit as st
import pandas as pd


st.title('❄️ How to connect Streamlit to a Snowflake database')

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")

# Load data table
@st.cache_data
def load_data(cc_form_results):
    ## Read in data table
    st.write(f"Here's some example data from `{cc_form_results}`:")
    table = session.table(cc_form_results)
    
    ## Do some computation on it
    table = table.limit(100)
    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Select and display data table
table_name = "CLOUD_DB.PUBLIC.CC_FORM_RESULTS"

## Display data table
with st.expander("See Table"):
    df = load_data(table_name)
    st.dataframe(df)

## Writing out data
for row in df:
    st.write(f"{row[0]} has a :{row[1]}:")
