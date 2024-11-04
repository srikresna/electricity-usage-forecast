# SUMMARY HASIL TRAINING DENGAN 4 MODEL

Berdasarkan pemodelan yang menggunakan empat model berbeda dan empat jenis data dengan fitur yang bervariasi, disimpulkan bahwa model `Bidirectional LSTM` menghasilkan performa terbaik dibandingkan model lainnya, terutama pada data gabungan Penggunaan Listrik dan Data Cuaca. Hasil ini ditunjukkan oleh nilai `Mean Absolute Error (MAE)` sebesar `0,06697`, `Mean Squared Error (MSE)` sebesar `0,07701` (semakin mendekati nol menunjukkan akurasi yang lebih baik), serta `R2 Score` sebesar `0,95717` (semakin mendekati satu menunjukkan kecocokan model yang lebih baik).

Jika dibandingkan dengan jenis data yang berbeda, performa `Bidirectional LSTM` tetapi masih tebukti unggul di 3 dari 4 jenis data yaitu: Data penggunaan listrik stasioner, Data penggunaan listrik mentah/standard, dan data gabungan penggunaan listrik dan data cuaca. Dapat diurutkan sebagai berikut

1. Data gabungan penggunaan listrik dan data cuaca (R2 score: 0.95716)
2. Data penggunaan listrik mentah/standard (R2 score: 0.94498)
3. Data penggunaan listrik stasioner (R2 score: 0.14192)

Sedangkan untuk data gabungan penggunaan listrik yang sudah di ektraksi fitur dan data cuaca, `Bidirectional LSTM` hanya mendapatkan `R2 score` sebesar `0.75866`. Data ini terbukti lebih bagus dimodelkan menggunakan `Bidirectional LSTM + Attention Mechanism` dengan perolehan `R2 score` sebesar `0.82370`.

## Dataset pengguna 15 menit + data cuaca + fitur ektraksi 

### LSTM

![alt text](img/image.png)

### BIDIRECTIONAL LSTM

![alt text](img/image-1.png)

### LSTM - ATTENTION MECHANISM 

![alt text](img/image-2.png)

### BIDIRECTIONAL LSTM - ATTENTION MECHANISM

![alt text](img/image-3.png)

## Dataset pengguna 15 menit + data cuaca

### LSTM

![alt text](img/image-4.png)

### BIDIRECTIONAL LSTM

![alt text](img/image-7.png)

### LSTM - ATTENTION MECHANISM 

![alt text](img/image-6.png)

### BIDIRECTIONAL LSTM - ATTENTION MECHANISM

![alt text](img/image-5.png)

## Dataset pengguna 15 menit stasioner

### LSTM

![alt text](img/image-12.png)

### BIDIRECTIONAL LSTM

![alt text](img/image-15.png)

### LSTM - ATTENTION MECHANISM 

![alt text](img/image-14.png)

### BIDIRECTIONAL LSTM - ATTENTION MECHANISM

![alt text](img/image-13.png)

## Dataset pengguna 15 menit

### LSTM

![alt text](img/image-8.png)

### BIDIRECTIONAL LSTM

![alt text](img/image-11.png)

### LSTM - ATTENTION MECHANISM 

![alt text](img/image-10.png)

### BIDIRECTIONAL LSTM - ATTENTION MECHANISM

![alt text](img/image-9.png)


