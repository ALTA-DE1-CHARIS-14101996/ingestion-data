import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BigInteger, DateTime, Float, Boolean

#read parquet data
def get_dataFrame():
    df = pd.read_parquet('../dataset/yellow_tripdata_2023-01.parquet',engine='fastparquet')
    return df
df = get_dataFrame()
print('Yellow Trip Data')
print('------------------------')
# print(df)
# print(df.dtypes)


#clean data
def get_manipulated_data(df):
    df = df.rename(columns={'VendorID' : 'Vendor_ID' ,'RatecodeID' : 'Rate_code_ID', 'PULocationID': 'PU_Location_ID','DOLocationID' : 'DO_Location_ID'})
    #Mengisi null value di tabel tertentu dengan nilai 0
    df[['Vendor_ID', 'passenger_count', 'PU_Location_ID', 'DO_Location_ID', 'payment_type']] = df[['Vendor_ID', 'passenger_count', 'PU_Location_ID', 'DO_Location_ID', 'payment_type']].fillna(0)
    #menghapus baris dari DataFrame yang berisi nilai null (NaN) 
    df.dropna(inplace=True) 
    #mengubah tipe data kolom
    df['Vendor_ID'] = df['Vendor_ID'].astype('int8')
    df['passenger_count'] = df['passenger_count'].astype('int8')
    df['PU_Location_ID'] = df['PU_Location_ID'].astype('int8')
    df['DO_Location_ID'] = df['DO_Location_ID'].astype('int8')
    df['payment_type'] = df['payment_type'].astype('int8')     

    df['store_and_fwd_flag'] = df['store_and_fwd_flag'].replace(['N', 'Y'], [False, True])
    df['store_and_fwd_flag'] = df['store_and_fwd_flag'].astype('boolean')

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    return df
clean_data = get_manipulated_data(df)
# print(clean_data.dtypes)
# print('------------------------')

#create connection
def get_postgres_con():
    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    database = 'mydb'
    port = '5432'

    conn_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(conn_string)
    return engine
postgres_conn = get_postgres_con()
print(postgres_conn)

#Define Schema
def load_to_postgres (engine):    
    df_schema = {
        'Vendor_ID'             : BigInteger,
        'tpep_pickup_datetime'  : DateTime,
        'tpep_dropoff_datetime' : DateTime,
        'passenger_count'       : BigInteger,
        'trip_distance'         : Float,
        'Rate_code_ID'          : Float,
        'store_and_fwd_flag'    : Boolean,
        'PU_Location_ID'        : BigInteger,             
        'DO_Location_ID'        : BigInteger,              
        'payment_type'          : BigInteger,              
        'fare_amount'           : Float,  
        'extra'                 : Float,   
        'mta_tax'               : Float,   
        'tip_amount'            : Float,   
        'tolls_amount'          : Float,    
        'improvement_surcharge' : Float,  
        'total_amount'          : Float,   
        'congestion_surcharge'  : Float,  
        'airport_fee'           : Float
    }
    #insert to postgres
    clean_data.to_sql(name='parquet', con=engine, if_exists='replace', index=False, schema='public', dtype= df_schema, method=None, chunksize=5000)

load_to_postgres(postgres_conn)