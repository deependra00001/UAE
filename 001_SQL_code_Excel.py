import os
import pandas as pd
#import pandasql as ps
import sqlite3
from datetime import datetime


# update the folder name
os.chdir(r'F:\Deependra\Data Scientist\001UAE\001_SQL_code_Excel') 

# Setting up SQLite3 DB 
db_sqlite3 = sqlite3.connect('Python.db')

df_customers=pd.read_csv("customers.csv")

#df=pd.read_excel("weather_data.xlsx","Sheet1")

# write DF to DB as table
df_customers.to_sql('customers',db_sqlite3,if_exists='replace')

datetime.now()

query = '''
select * from customers
where "Customer Phone" ='4567895647'
'''

print(pd.read_sql(query,db_sqlite3))

query = '''
SELECT * FROM sqlite_master
'''

print(pd.read_sql (query,db_sqlite3))



datetime.now()
df_cbg_b25=pd.read_csv("cbg_b25.csv")
datetime.now()

# write DF to DB as table
df_cbg_b25.to_sql('cbg_b25',db_sqlite3,if_exists='replace',chunksize =10000)
datetime.now()