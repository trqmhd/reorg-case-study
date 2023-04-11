import pandas as pd
import os
import zipfile
import urllib.request
from sqlalchemy import create_engine, text

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

connection_string = os.environ.get('LOCAL_SQLALCHEMY_DATABASE_URI')
engine = create_engine(connection_string)

def update_data():
    # Download the data
    # URL to the zip file
    url = "https://download.cms.gov/openpayments/PGYR20_P012023.ZIP"

    # Download the zip file
    urllib.request.urlretrieve(url, 'openPaymentData.zip')

    # Extract the contents of the zip file
    with zipfile.ZipFile('openPaymentData.zip', 'r') as zip_ref:
        zip_ref.extractall('openPaymentData')

    script_path = os.path.abspath(__file__)

    # Get the folder path of the current script
    folder_path = os.path.dirname(script_path)

    prefix = "OP_DTL_GNRL_"

    # List all files in the specified folder
    all_files = os.listdir(folder_path + '/openPaymentData')

    # Find the first file that starts with the specified prefix
    matching_file = None
    for file in all_files:
        if file.startswith(prefix):
            matching_file = file
            break
    csv_file_path = str(folder_path + '/openPaymentData/' + matching_file)

    # Define the chunk size (number of rows to read at a time)
    chunk_size = 10000
    table_name = "payment"
    print ("Data is being Updated...")
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
                    connection.execute(update_query, query_params)

        # Insert rows
        if not rows_to_insert.empty:
            rows_to_insert.to_sql(name=table_name, con=engine, if_exists='append')

    # Close the SQLAlchemy engine
    engine.dispose()

if __name__ == '__main__':
    update_data()