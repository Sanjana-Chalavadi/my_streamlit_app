# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit
import streamlit as st
import pandas as pd
import snowflake.connector


st.title('Cloud Computing Form Table')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
