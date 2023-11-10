from sqlalchemy import create_engine, MetaData,Table,Column,ForeignKey,insert,text

# Membuat koneksi ke PostgreSQL
user = 'postgres'
password = 'pass'
host = 'localhost'
database = 'task4'
port = '5432'

conn_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine1= create_engine(conn_string)
source_metadata = MetaData()
source_metadata.reflect(bind=engine1)
pg_conn = engine1.connect()
    

# Membuat koneksi ke Citus
user = 'postgres'
password = 'pass'
host = 'localhost'
database = 'task4'
port = '15432'

conn_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine2 = create_engine(conn_string)
dest_metadata = MetaData()
dest_metadata.reflect(bind=engine2)
ct_conn = engine2.connect()

# Daftar tabel yang akan ingest
tables = ['brands', 'products', 'orders', 'order_details'] 

# Membuat fungsi pengecekan table
for table in tables:
    source_table = Table(table,source_metadata)
    dest_table = Table(table,dest_metadata)
     
    for kolom in source_table.columns:
        column = Column(kolom.name,kolom.type)
        if kolom.primary_key :
            column.primary_key = True
        if kolom.foreign_keys :
            foreign_key_column = list(kolom.foreign_keys)[0]
            ref_table = foreign_key_column.column.table.name
            dest_column = foreign_key_column.column.name
            column.append_foreign_key(ForeignKey(f'{ref_table}.{dest_column}'))
        if not kolom.nullable:
            column.nullable = False
            
        dest_table.append_column(column)
    dest_table.create(engine2)
query = text('alter table orders alter column order_date set default current_timestamp;')
ct_conn.execute(query)

#ingest data
for table in tables:
    source_table = Table(table,source_metadata)
    dest_table = Table(table,dest_metadata)
    select = source_table.select()
    data = pg_conn.execute(select)
    
    for row in data:
        ingest = insert(dest_table).values(row)
        ct_conn.execute(ingest)
        ct_conn.commit()
 


    