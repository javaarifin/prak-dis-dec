# prak-dis-dec
# Laporan Praktikum PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI #

---
## Minggu 2

------
Nama    : Muhammad Java Arifin

NIM     : 235410073

-----
 ## Komunikasi Antar Proses pada Sistem Terdistribusi



Pengantar

Proses merupakan hasil dari eksekusi program / aplikasi yang bersifat executable.
Proses dikelola oleh sistem operasi dan terdiri atas executable code, data, resources, serta
informasi tentang state (stack dan heap). Setiap aplikasi yang dijalankan akan menjadi
proses.

### Proses pada Satu Node
 Pada satu node, semua akan berada dalam kendali sistem operasi: eksekusi
 menjadi proses, alokasi resources, pengelolaan proses, serta komunikasi antar proses. Hal
 ini bersifat transparan terhadap pengguna (artinya pengguna tidak perlu melihat, tapi di latar
 belakang proses ini dikelola oleh sistem operasi)

### Tugas

### 1. Tampilkan berbagai proses yang ada pada komputer yang    anda gunakan sesuaidengan sistem operasi yang anda gunakan.
Disini saya memakai sistem oprasi windows cara untuk melihat berbagai proses di task manager bisa dengan cara tekan pada keyboard ctrl+shift+esc dengan menekan tombol itu berbarengan akan menampilkan task manager dan anda bisa melihat berbagai proses yang ada pada komputer yang anda gunakan
    
![tampilan proses](Images/aplikasi%20capcut.png)
    Gambar diatas merupakan gambar task manager yang menampilkan berbagai proses pada komputer saya 

### 2. Jalankan salah satu aplikasi, perlihatkan proses yang dimunculkan oleh aplikasi tesebut.
![menjalankan aplikasi](Images/Screenshot%202026-03-31%20085153.png)
aplikasi yang dijalankan adalah capcut editing video dan dari tampilan gambar diatas menunjukan aplikasi ini menggunakan sumber daya sistem sebagai berikut :
* CPU: sebesar 6,8%
* Memori (RAM): sebesar 1.379,2 MB (±1,3 GB)
* Disk: sebesar 2,3 MB/s
* Jaringan (Network): sebesar 2,9 Mbps

### 3. Carilah petunjuk untuk: me-restart proses dan mematikan proses. Matikan proses yang dimunculkan oleh aplikasi yang anda jalankan, jangan gunakan perintah untuk keluar dari aplikasi yang anda jalankan tetapi gunakan perintah untuk mematikan proses dari aplikasi yang anda jalankan.
![](Images/end%20task.png)
Gambar diatas merupakan proses aplikasi capcut sebelum di matikan prosesnya,di sistem oprasi windows untuk mematikan proses di task manager dengan cara klik kana aplikasi yang mau di matikan prosesnya dan pilih opsi "end task" setelah di end task maka aplikasi tersebut akan mematikan prosesnya di dalam komputer berikut gambar hasil setelah dimatika porsesnya

![](Images/Screenshot%202026-03-31%20085153.png)
Setelah aplikasi di end task maka akan terlihat tidak memakan sumber daya komputer

### 4. Jelaskan semua hal yang anda kerjakan tersebut.
Untuk membuka task manager di sistem oprasi windows bisa dengan short cut "ctr+shift+esc" dengan task manager saya dapat melihat berbagai komunikasi antar proses. saya mencoba membuka aplikasi CapCut editor video dan saya dapa melihat detail sumber daya yang digunakan aplikasi ini. Dan saya juga mencoba untuk mematikan proses dengan cara end task di task manager 

##   Menggunakan Strawberry untuk GraphQL Server
Berikut langkah-langkah praktik yang bisa dikerjakan:
### 1. Pelajari cara menggunakan uv. Lihat catatan di 
    https://github.com/NEO-X-School/notes/blob/main/uv/00.md.
### 2. Buat workspace dengan nama workspace-01. Pada workspace tersebut, gunakan Python versi 3.14.3 (lihat petunjuk di atas).
### 3. Buat environment, aktifkan environment yang sudah anda     buat tersebut.
### 4. Instalasi paket-paket yang diperlukan:


