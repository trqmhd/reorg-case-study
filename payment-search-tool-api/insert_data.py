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

def insert_data():
    # Download the data
    # URL to the zip file
    url = "https://download.cms.gov/openpayments/PGYR20_P012023.ZIP"

    # Download the zip file
    print ("Downloading Zip file...")
    urllib.request.urlretrieve(url, 'openPaymentData.zip')

    # Extract the contents of the zip file
    with zipfile.ZipFile('openPaymentData.zip', 'r') as zip_ref:
        zip_ref.extractall('openPaymentData')
    print ("Zip file extracted...")


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
    min_cost = 10
    table_name = "payment"
    print ("Data in being inserted...")
    # Loop through the CSV file in chunks
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size, low_memory=False):
        # Filter the data to find records where a doctor accepted gifts costing more than $10
        filtered_chunk = chunk[chunk["Total_Amount_of_Payment_USDollars"] > min_cost]
        # filtered_chunk.replace([np.inf, -np.inf], np.nan, inplace=True)
        
        # define a lambda function to truncate column names
        truncate_colname = lambda x: x[:64]

        # use rename method with the lambda function to truncate all column names
        filtered_chunk = filtered_chunk.rename(columns=truncate_colname)

        cols_to_string = filtered_chunk.columns[filtered_chunk.columns != 'Record_ID']
        filtered_chunk[cols_to_string] = filtered_chunk[cols_to_string].astype(str)

        # Store the filtered data in the MySQL table using SQLAlchemy's to_sql() method
        filtered_chunk.to_sql(name=table_name, con=engine, if_exists="append", index=False)

    with engine.connect() as connection:
        connection.execute(text(f'ALTER TABLE {table_name} ADD PRIMARY KEY (`Record_ID`);'))

    # Close the SQLAlchemy engine
    engine.dispose()

if __name__ == '__main__':
    insert_data()