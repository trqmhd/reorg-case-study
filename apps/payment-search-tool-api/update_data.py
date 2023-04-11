# import mysql.connector
import pandas as pd
from io import StringIO
import os
import zipfile
import tempfile
import numpy as np
import urllib, requests
from sqlalchemy import Integer, create_engine, Text, text

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


connection_string = os.environ.get('LOCAL_SQLALCHEMY_DATABASE_URI')
engine = create_engine(connection_string)

def import_data():
    # Download the data
    # URL to the zip file
    # url = "https://download.cms.gov/openpayments/PGYR20_P012023.ZIP"

    # # # Download the zip file
    # print ("Downloading...")
    # urllib.request.urlretrieve(url, 'openPaymentData.zip')

    # # # Extract the contents of the zip file
    # with zipfile.ZipFile('openPaymentData.zip', 'r') as zip_ref:
    #     zip_ref.extractall('openPaymentData')
    # print ("Extracted...")

    # Define the path to the CSV file
    # csv_file_path = "/backend-app/openPaymentData/OP_DTL_GNRL_PGYR2020_P01202023.csv"
    csv_file_path = "/Users/tariq/Documents/reorg-case-study-main/apps/payment-search-tool-api/openPaymentData/OP_DTL_GNRL_PGYR2020_P01202023.csv"


    # Define the chunk size (number of rows to read at a time)
    chunk_size = 10000
    table_name = "payment"
    print ("Data is being Updated...")

#   # Read only the header row of the CSV file
#     with open(csv_file_path) as f:
#         header = pd.read_csv(f, nrows=0).columns.tolist()
#     print(header)
    # Loop through the CSV file in chunks
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size, low_memory=False):
        # Filter the data to find records where a doctor accepted gifts costing more than $10
        filtered_chunk = chunk[chunk["Total_Amount_of_Payment_USDollars"] > 15000]
        
        # filtered_chunk.replace([np.inf, -np.inf], np.nan, inplace=True)
        
        # define a lambda function to truncate column names
        truncate_colname = lambda x: x[:64]

        # use rename method with the lambda function to truncate all column names
        filtered_chunk = filtered_chunk.rename(columns=truncate_colname)

        filtered_chunk = filtered_chunk.astype(str)
        # print (filtered_chunk.head())

        # filtered_chunk.set_index('Record_ID', inplace=True)

        # print (filtered_chunk.columns)

        rows_to_update = filtered_chunk[(filtered_chunk.Change_Type == 'CHANGED') | (filtered_chunk.Change_Type == 'ADD')]
        rows_to_insert = filtered_chunk[filtered_chunk.Change_Type == 'NEW']

        # Update rows
        with engine.connect() as connection:
            if not rows_to_update.empty:
                for index, row in rows_to_update.iterrows():
                    # Generate the SET clause dynamically
                    set_clause = ', '.join([f"{column} = :{column}" for column in row.index if column != 'Record_ID'])
                    update_query = text(f"UPDATE {table_name} SET {set_clause} WHERE Record_ID=:record_id")

                    # Generate the query parameters dynamically
                    query_params = {f"{column}": row[column] for column in row.index if column != 'Record_ID'}
                    query_params['record_id'] = row['Record_ID']
                    print(update_query)
                    print(query_params)

                    connection.execute(update_query, **query_params)




        # Insert rows
        if not rows_to_insert.empty:
            rows_to_insert.to_sql(name=table_name, con=engine, if_exists='append')

        # # # Store the filtered data in the MySQL table using SQLAlchemy's to_sql() method
        # # filtered_chunk.to_sql(name=table_name, con=engine, if_exists="append", index=False)

    # Close the SQLAlchemy engine
    engine.dispose()



if __name__ == '__main__':
    import_data()