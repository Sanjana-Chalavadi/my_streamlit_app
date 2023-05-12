# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit as st
import pandas as pd
import snowflake.connector


st.title('Cloud Computing Form Table')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from cc_form_results")
my_data_row = my_cur.fetchone()
st.text("Form table display success")
st.text(my_data_row)
#make it look like a dataframe
st.dataframe(my_data_row)
