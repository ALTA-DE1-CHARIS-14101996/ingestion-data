import pandas as pd

# Read Data
df = pd.read_csv("../dataset/yellow_tripdata_2020-07.csv", sep=",")
print("Dataset Yellow Trip Data")
print(df) 
print('-----------------------------------------')

# Rename Column
print(df.dtypes) 
rename_column = df.rename(columns={'VendorID' : 'Vendor_ID' ,'RatecodeID' : 'Rate_code_ID', 'PULocationID': 'PU_Location_ID','DOLocationID' : 'DO_Location_ID'})
print(rename_column.dtypes)

#Menampilkan  10 Data teratas dari table passenger_count dan hanya menampilkan table tertentu
# Pilih Top 10 Passenger Count tertinggi
top_passenger_counts = rename_column.nlargest(10, 'passenger_count')

# Pilih Kolom lain yang ingin ikut di tampilkan
selected_columns = ['Vendor_ID', 'passenger_count', 'trip_distance', 'payment_type', 'fare_amount', 'extra', 'mta_tax',
                    'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount', 'congestion_surcharge']

result = top_passenger_counts[selected_columns]
# Menampilkan Hasil Output
print(result)

#Mengubah tipe data pada kolom
rc = rename_column
rc[['Vendor_ID', 'passenger_count', 'PU_Location_ID', 'DO_Location_ID', 'payment_type']] = rc[['Vendor_ID', 'passenger_count', 'PU_Location_ID', 'DO_Location_ID', 'payment_type']].fillna(0)
rc['Vendor_ID'] = rc['Vendor_ID'].astype(int)
rc['passenger_count'] = rc['passenger_count'].astype(int)
rc['PU_Location_ID'] = rc['PU_Location_ID'].astype(int)
rc['DO_Location_ID'] = rc['DO_Location_ID'].astype(int)
rc['payment_type'] = rc['payment_type'].astype(int)     

rc['store_and_fwd_flag'] = rc['store_and_fwd_flag'].replace(['N', 'Y'], [False, True])
rc['store_and_fwd_flag'] = rc['store_and_fwd_flag'].astype(bool)

rc['tpep_pickup_datetime'] = pd.to_datetime(rc['tpep_pickup_datetime'])
rc['tpep_dropoff_datetime'] = pd.to_datetime(rc['tpep_dropoff_datetime'])

print(rc.dtypes)

