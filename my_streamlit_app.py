# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit
from snowflake.snowpark.session import Session
import streamlit as st
import pandas as pd


st.title('Cloud Computing Form Table')

# Create Session object
def create_session_object():
   connection_parameters = {
      "account": "HLB87172",
      "user": "sanjanachalavadi95",
      "password": "Snowflake999*",
      "role": "PC_RIVERY_ROLE",
      "warehouse": "COMPUTE_WH",
      "database": "CLOUD_DB",
      "schema": "PUBLIC"
   }
   session = Session.builder.configs(connection_parameters).create()
   return session

#Load data in snowpark dataframes
# Create Snowpark DataFrames that loads data from CLOUD_DB
def load_data(table_name):
    # read in data table
   snow_df = session.table(table_name)
   #collect the results
   snow_df = snow_df.collect()
   # Convert Snowpark DataFrames to Pandas DataFrames for Streamlit
   pd_df = snow_df.to_pandas()

   return pd_df

#writing out the data
for row in pd_df:
   st.write(f"{row[0]} has a row :{row[1]}:")
