 LAPORAN PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI #

---
## Minggu 5

------
Nama    : Muhammad Java Arifin

NIM     : 235410073

-----
## Cloud Computing

### Pengantar
Cloud Computing menggunakan pendekatan XaaS atau sering juga disebut sebagai
Everything as a Service. Dengan menggunakan pendekatan ini, provider dari Cloud
Computing menyediakan berbagai sumber daya komputasi dan konsumen mendapatkan
sumber daya tersebut dalam bentuk layanan. Meskipun saat ini ada banyak XaaS tetapi
secara umum biasanya dibagi menjadi 3:

1. SaaS: Software as a Service
2. PaaS: Platform as a Service
3. IaaS: Infrastructure as a Service


### 1.Persiapan Aplikasi Flask
- Jalankan Docker Dekstop
- Mengambil kode sumber dan membuat folder:

        # Clone repositori Flask
        git clone https://github.com/pallets/flask

        # Buat folder baru
        mkdir flask-app

        # Copy isi folder tutorial ke dalam folder flask-app
        Copy-Item -Path .\flask\examples\tutorial\* -Destination .\flask-app\ -Recurse

        # Masuk ke folder aplikasi
        cd flask-app