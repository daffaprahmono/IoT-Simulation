# IoT-Simulation
Projek ini menyimulasikan pengambilan data dari sensor yang diletakkan pada suatu ruangan yang bertujuan untuk memonitoring **Suhu**, **Kelembapan**, dan **Intensitas Cahaya** pada ruangan tersebut.

Tujuan dibuatnya projek ini adalah untuk meningkatkan skill serta pemahaman mengenai dasar-dasar python programming, dan juga menambah pengalaman dalam membuat program.

Projek ini dibuat menggunakan bahasa pemrograman **Python** yang terdiri dari 4 file:
* processor.py
* temp_sensor.py
* humidity_sensor.py
* light_sensor.py

### Penjelasan Tiap File
#### 1. processor.py
File ini merupakan kode utama letak fungsi main(). Pada file ini terdapat fungsi-fungsi utama seperti pengklasifikasian data, data processing, dan data plotting. Data-data yang diambil dari file lain diolah di file ini.
#### 2. temp_sensor.py
File ini merupakan kode yang menyimulasikan sensor suhu yang digunakan pada kode program utama. Suhu didefinisikan dengan nilai awal 25 &deg;C, nilai minimum 15 &deg;C, dan nilai maksimum 30 &deg;C. Pada file ini juga terdapat kode program untuk meng-*generate* nilai suhu dengan perubahan yang terukur, yaitu -5 dan +5 dari nilai awal. Karena nilai suhu menggunakan tipe data float, maka dibulatkan dengan 1 angka dibelakang koma.
#### 3. humidity_sensor.py
File ini merupakan kode yang menyimulasikan sensor kelembapan yang digunakan pada kode program utama. Kelmbapan didefinisikan dengan nilai awal 45%, nilai minimum 30%, dan nilai maksimum 60%. Pada file ini juga terdapat kode program untuk meng-*generate* nilai kelembapan dengan perubahan yang terukur, yaitu -10 dan +10 dari nilai awal.
#### 4. temp_sensor.py
File ini merupakan kode yang menyimulasikan sensor cahaya yang digunakan pada kode program utama. Intensitas cahaya didefinisikan dengan nilai awal 1080 lux, nilai minimum 540 lux, dan nilai maksimum 1620 lux. Pada file ini juga terdapat kode program untuk meng-*generate* nilai intensitas cahaya dengan perubahan yang terukur, yaitu -360 dan +360 dari nilai awal.
