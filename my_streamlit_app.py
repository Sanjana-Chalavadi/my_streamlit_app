# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit
#from snowflake.snowpark.session import Session
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
def load_data(session):
    # FORM RESULTS TBLE
    snow_df = session.table("CC_FORM_RESULTS")
 
    # Convert Snowpark DataFrames to Pandas DataFrames for Streamlit
    pd_df = snow_df.to_pandas()


if __name__ == "__main__":
    session = create_session_object()
    load_data(session)
