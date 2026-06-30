## LAPORAN PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

### NAMA    : Muhammad Java Arifin

### NIM     : 235410073

### Konsensus pada Blockchain (Solana)

Praktikum ini bertujuan untuk mengeksplorasi dan mengimplementasikan jaringan blockchain menggunakan platform Solana. Solana merupakan platform blockchain yang dirancang khusus untuk mengatasi masalah skalabilitas tanpa mengorbankan keamanan atau desentralisasi. Berbeda dengan blockchain tradisional, Solana mampu memproses hingga puluhan ribu transaksi per detik (TPS) dengan biaya yang sangat murah. Keunggulan ini membuatnya ideal untuk aplikasi terdesentralisasi (dApps), decentralized finance (DeFi), dan pasar NFT

### 1. Instalasi dan Persiapan Lingkungan Pengembangan

Bagian pertama dari praktikum ini adalah melakukan instalasi perangkat lunak yang dibutuhkan untuk pengembangan aplikasi di jaringan Solana.


* Rust

    ![](Images/rust%20version.png)

* Node.js

    ![](Images/node.png)

### A. Instalasi Solana CLI 

Solana CLI diinstal dan dikonfigurasi ke dalam variabel environment PATH. Selain itu, praktikum ini juga menggunakan Anchor, yaitu sebuah framework untuk DApp berbasis Solana. Instalasi Anchor dilakukan menggunakan avm (Anchor Version Manager).

Untuk mulai menggunakan Solana, kita akan melakukan instalasi software Solana, khususnya
yang digunakan untuk pengembangan aplikasi. Beberapa prasyarat yang harus diinstall terlebih
dahulu adalah:


* Install solana

    ![](Images/solana.png)

Daftarkan path Solana CLI secara permanen ke profil shell WSL Anda:

![](Images/daftar%20wsl.png)

### B. Instalasi Anchor Version Manager (AVM)

#### 1. Unduh dan pasang AVM menggunakan skrip resmi:

![](Images/avm.png)

#### 2. Daftarkan letak binari AVM ke dalam environmen

![](Images/daftar.png)

#### 3.Unduh dan gunakan framework Anchor versi terbaru melalui AVM:
![](Images/achr.png)

#### 4. erifikasi instalasi Anchor:

![](Images/achrversi.png)

### 2. Pembuatan Alamat Wallet Solana

Wallet 1 (Akan digunakan sebagai Default Wallet)
![](Images/wallet1.png)

Wallet 2 (Alamat Tujuan Uji Coba)
![](Images/wallet2.png)

Konfigurasi Default Keypair
![](Images/konf.png)

### 3. Konfigurasi Jaringan & Klaim SOL (Devnet)
Hubungkan ke Jaringan Devnet Solana
Ubah target RPC cluster Solana dari lokal/mainnet menuju kluster uji coba (Devnet):
![](Images/targetrpc.png)

Meminta Airdrop SOL Uji Coba
![](Images/minta.png)

![](Images/solana21.png)

![](Images/tf.png)

### 4. Alur Pengujian Konsensus & Transaksi

Langkah 1: Transfer Antar Wallet

Kirimkan sejumlah 0.5 SOL dari dompet default menuju dompet kedua. Gunakan flag --allow-unfunded-recipient karena akun tujuan belum memiliki saldo awal:

![](Images/tfantrwlt.png)

Langkah 2: Eksplorasi Detail Blok & Validator Jaringan
Guna mempelajari gabungan mekanisme Proof of History (PoH) dan Proof of Stake (PoS) pada Solana, jalankan perintah eksaminasi data berikut:

![](Images/dftr.png)
