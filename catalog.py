mport streamlit

streamlit.title('Zenas Online Catalog')

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor ()

my_cur.execute("select current_user(), current_account(), current_region()")

my_data_row = my_cur.fetchone()

streamlit.txt("Hello from Snowflake:")
streamlit.txt(my_data_row)
