# Modified from Johannes Rieke's example code
# Import required libraries
import streamlit
import pandas as pd
import snowflake.connector


streamlit.title('Cloud Computing Form Table')
#connects to the database
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#queries the table
my_cur.execute("select * from cloud_db.public.cc_form_results")
my_data_rows = my_cur.fetchall()
streamlit.text("Form table display success")
#make it look like a dataframe
streamlit.dataframe(my_data_rows)
