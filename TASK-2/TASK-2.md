# TASK 2
1. We are going to create a DataFrame from a parquet file on our datasets. (file yellow_tripdata_2023-01.parquet)
    (mirip dengan file test.py tapi ganti format ke parquet dan tambah/import dengan library sesuai nomor selanjutnya (nomor 1-5))
2. Load the parquet file to a DataFrame with fastparquet library.

3. Clean the Yellow Trip dataset.

4. Define the data type schema when using to_sql method.
    
5. Ingest the Yellow Trip dataset to PostgreSQL

6. Count how many rows are ingested.
    (masuk ke dbeaver use count(SQL))

# Answer
Untuk menjawab semua soal tersebut, berikut tahapan yang saya lakukan:
1. Pertama kita buat file python yang berfungsi untuk mengakses file parquet dan membuatnya menjadi sebuah dataframe, seperti yang telah saya buat yaitu file df_parquet_to_postgres.py.
    Disini kita menggunakan metode fastparquet.

    ![Alt text](image.png)

    ![Alt text](image-1.png)

2. Kemudian kita perlu melakukan cleaning data dengan melakukan standarisasi format pada kolom dan tipe data dan juga melakukan sesuatu terhadap null value.
    Melakukan pengecekan nama tabel dan tipe data.

    ![Alt text](image-2.png)

    Melakukan cleaning data

    ![Alt text](image-3.png)

    Hasil setelah dilakukan perubahan

    ![Alt text](image-4.png)


3. Setelah itu sebelum kita melakukan define schema kita perlu membuat fungsi untuk mengkoneksikannya dengan postgresql seperti gambar berikut.

    ![Alt text](image-5.png)
    
    Barulah kita bisa mendefinisikan schema yang akan kita masukkan ke database postgre dan membuat membuat fungsi .to_sql untuk melakukan koneksi ke postgre.

    ![Alt text](image-6.png)

4. Sebelum kita menjalankan python ini kita perlu memastikan docker desktop kita sudah berjalan dan terdapat image2 yang kita perlukan.

    ![Alt text](image-7.png)

    Siapkan file docker compose yang sudah terkonfigurasi dan siap dijalankan. Pastikan file tersebut berlokasi sama dengan work directory saat ini. Kemudian lakukan perintah di bawah ini.
    
     
     ```
     docker compose <nama-file> up -d
     ```
    Namun perlu dipastikan port yang akan digunakan sedang tidak terpakai dan tidak ada docker lain yang berjalan sebelum menjalankannya.

    ![Alt text](image-8.png)

    Pastikan semua container berjalan dengan melihat dengan menjalankan perintah
    ```
     docker ps
     ```
    Atau dengan melihat di aplikasi desktop.

    ![Alt text](image-9.png)

    Koneksikan dbeaver dengan container yang telah terbuat.

    ![Alt text](image-10.png)

    Sesuaikan konfigurasi dengan python dan file docker compose yang telah dibuat

    ![Alt text](image-11.png)

    Jika sudah terkoneksi maka database akan terbentuk di dbeaver

    ![Alt text](image-12.png)

5. Selanjutnya ingest file parquet ke dalam postgres yang telah di buat dengan menjalankan file python yang telah kita buat tadi.
    ```
     $ python df_parquet_to_postgres.py
    ```

    ![Alt text](image-13.png)

    Cek file di database

    ![Alt text](image-14.png)

    Dapat dilihat diatas bahwa file sudah masuk ke database.

6. Sekarang kita akan menghitung berapa banyak row yang ter-ingest ke database tersebut dengan menjalankan perintah berikut .

     ```
     SELECT COUNT(*) AS TOTAL_ROW FROM parquet ;
     ```
    Dapat kita lihat total row yang ter-ingest ada 100.000 row

    ![Alt text](image-15.png)

# END