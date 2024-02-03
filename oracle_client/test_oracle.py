from sqlalchemy import create_engine
import pandas as pd

# engine = create_engine('oracle+cx_oracle://back:back@10.32.59.171:1521/?service_name=datalake')
engine = create_engine('oracle+cx_oracle://dev_viewer:dev_viewer@10.32.59.85:1521/?service_name=trading')

df = pd.read_sql_query('select * from BACK.T_CUST_CUSTOMER FETCH FIRST 5 ROWS ONLY', engine)
print(df)