### LSTM Modeling

* `standard.ipynb` standard data tanpa fitur cuaca dan fitur engineering.

* `standard_stationary` standard data yang sudah di differencing menjadi stasioner lalu di training.

* `standard_weather` standard data dengan fitur cuaca.

* `standard_weather_feature` standard data + fitur cuaca + fitur engineering, belum maksimal (`steps_per_epoch = 280`) karena ukuran terlalu besar untuk di proses di GPU Colab.