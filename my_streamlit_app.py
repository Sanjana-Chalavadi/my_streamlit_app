# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit
import pandas as pd
import snowflake.connector


streamlit.title('Cloud Computing Form Table')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from cloud_db.public.cc_form_results")
my_data_row = my_cur.fetcall()
streamlit.text("Form table display success")
streamlit.text(my_data_row)
#make it look like a dataframe
streamlit.dataframe(my_data_row)
