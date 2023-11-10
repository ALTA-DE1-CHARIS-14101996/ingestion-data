# TASK 1
1. We have already learned how to create DataFrame from files here. Now, we are going to create a DataFrame from a larger csv file on our datasets.
    1. Pertama kita buat file python yang berfungsi untuk mengakses file csv dan membuatnya menjadi sebuah dataframe, seperti yang telah saya buat yaitu file df_from_csv.py

        ![Alt text](image.png)
    2. Kemudian Jalankan File tersebut untuk melihat hasilnya

        ![Alt text](image-1.png)

2. Rename all the columns with snake_case format.
    1. Untuk mengecek nama tiap kolom pada file ada beberapa cara, untuk ini saya akan menggunakan perintah dtypes untuk melihat nama kolom pada file tersebut.

        ![Alt text](image-2.png)

        ![Alt text](image-3.png)
    2. Kemudian kita ubah semua nama kolom yang belum menggunakan snakecase format --> snake case format dengan syntax sebagai berikut. Kemudian kita jalankan untuk melihat hasilnya.

        ![Alt text](image-4.png) 

        ![Alt text](image-5.png)

3. Select only 10 top of highest number of passenger_count, show only columns vendor_id, passenger_count, trip_distance, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount,improvement_surcharge, total_amount, congestion_surcharge from the DataFrame.

    ![Alt text](image-6.png)

    ![Alt text](image-7.png)

4. [Extra] Cast the data type to the appropriate value.
    1. Pertama Kita cek dahulu tipe data masing-masing kolom menggunakan dtypes.

        ![Alt text](image-8.png)
    2. kemudian Kita ubah jika ada kolom yang sekiranya memiliki tipe data yang kurang sesuai dengan perintah berikut. Sehingga dapat kita lihat hasil perubahannya.
        ![Alt text](image-9.png)
        ![Alt text](image-10.png)

# END

