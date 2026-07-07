## LAPORAN PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

### NAMA    : Muhammad Java Arifin

### NIM     : 235410073

### Topik: Smart Contract pada Blockchain (Solana & Ekosistem Alternatif)
#### Modul: 14


#### RINGKASAN PRAKTIKUM
Praktikum minggu ini berfokus pada pemahaman dan praktik langsung pembuatan smart contract (program) di dalam arsitektur blockchain. Pada ekosistem Solana, pengembangan dilakukan menggunakan bahasa Rust melalui dua pendekatan berbeda: metode Native Rust murni dan penggunaan Anchor Framework. Sebagai tambahan eksplorasi, dilakukan juga uji coba pembuatan smart contract pada ekosistem blockchain Layer 1 alternatif, yaitu Jaringan Sui.

#### BAGIAN 1: PENGEMBANGAN SOLANA MENGGUNAKAN NATIVE RUST
Pendekatan native mengharuskan pengembang untuk menginisialisasi pustaka Rust secara manual dan mengonfigurasi kompilator agar menghasilkan shared object (SBF).

##### Persiapan Proyek dan Dependensi
Proyek library baru dibuat menggunakan Cargo, dilanjutkan dengan penambahan pustaka inti Solana dan modul pengujian (litesvm serta solana-sdk).

    cargo new hello_solana --lib

![](Images/Screenshot%202026-07-07%20203227.png)


    cd hello_solana
    cargo add solana-program

![](Images/Screenshot%202026-07-07%20203452.png)


        cargo add litesvm --dev

![](Images/Screenshot%202026-07-07%20203642.png)
![](Images/Screenshot%202026-07-07%20203658.png)

    cargo add solana-sdk --dev

![](Images/Screenshot%202026-07-07%20203949.png)


##### Edit Cargo.toml, tambahkan
    [lib]
    crate-type = ["cdylib", "lib"]
![](Images/Screenshot%202026-07-07%20204315.png)

##### Ganti src/lib.rs dengan source code berikut:

    use solana_program::{
        account_info::AccountInfo, entrypoint, entrypoint::ProgramResult, msg, pubkey::Pubkey,
    };

    entrypoint!(process_instruction);

    pub fn process_instruction(
        _program_id: &Pubkey,
        _accounts: &[AccountInfo],
        _instruction_data: &[u8],
    ) -> ProgramResult {
        msg!("Hello, world!");
        Ok(())
    }
    
![](Images/Screenshot%202026-07-07%20204601.png)

Build source code smart contract tersebut menggunakan perintah cargo build-sbf. Perintah ini
spesifik untuk Solana. Saat mengerjakan perintah tersebut, cargo akan menginstall semua tools yang
diperlukan (jika belum ada)

    cargo build-sbf

![](Images/Screenshot%202026-07-07%20205422.png)
![](Images/Screenshot%202026-07-07%20205455.png)
Hasilnya bisa dilihat pada direktori target/deploy:
![](Images/Screenshot%202026-07-07%20205725.png)


Pengujian Lingkungan (Testing)
Sebelum deployment nyata, smart contract diuji secara lokal. Skrip testing diletakkan pada tests/lib_test.rs. Eksekusi pengujian dilakukan dengan perintah:

    cargo test -- --show-output
![](Images/Screenshot%202026-07-07%20210031.png)

Deployment ke Localhost
Proses ini membutuhkan dua jendela terminal (Command Prompt/PowerShell):

* Terminal 1: Menjalankan validator lokal untuk simulasi blockchain.

    solana-test-validator
![](Images/Screenshot%202026-07-07%20222325.png)

* Terminal 2: Mengubah konfigurasi jaringan ke localhost, lalu meluncurkan smart contract.

    solana config set -ul
    solana program deploy target/deploy/hello_solana.so

![](Images/Screenshot%202026-07-07%20223108.png)

![](Images/Screenshot%202026-07-07%20223007.png)

Untuk melihat block, akses ke
https://explorer.solana.com/?cluster=custom&customUrl=http%3A%2F%2Flocalhost%3A8899

dengan memasukan program ID 
![](Images/Screenshot%202026-07-07%20223652.png)

tetapi gambar saya diatas memuat loading terus.

akhirnya saya menggunakan perintah di wsl 

     solana account C54bHCXEGZKG9JwnHecpfuhxwyR8Gug1Sv4apyXQZVWQ

![](Images/Screenshot%202026-07-07%20223948.png)

#### PENGEMBANGAN SOLANA MENGGUNAKAN ANCHOR FRAMEWORK

Anchor menyediakan tingkat abstraksi yang lebih tinggi, memungkinkan pengembangan smart contract yang lebih terstruktur dan efisien berkat CLI dan makro bawaan.

#### Pembuatan Proyek Anchor

Inisialisasi proyek dilakukan dengan memanfaatkan templat mollusk agar pengujian otomatis terkonfigurasi dalam bahasa Rust.

    anchor init --test-template mollusk sc-solana 
![](Images/Screenshot%202026-07-07%20224340.png)

    cd sc-solana

![](Images/Screenshot%202026-07-07%20224433.png)

Setelah diinisialisasi, program langsung di-build:

    anchor build
![](Images/Screenshot%202026-07-07%20224818.png)

Eksekusi Pengujian Anchor

    anchor test

![](Images/Screenshot%202026-07-07%20225857.png)


Deployment ke Jaringan Devnet

    solana config set --url devnet
    anchor program deploy
![](Images/Screenshot%202026-07-07%20230921.png)

![](Images/Screenshot%202026-07-07%20231019.png)

![](Images/Screenshot%202026-07-07%20231533.png)

#### Kesimpulan 

Kesimpulan
Berdasarkan serangkaian langkah dan uji coba yang telah dilakukan pada Praktikum Modul 14 ini, dapat ditarik beberapa kesimpulan utama mengenai pengembangan smart contract pada ekosistem blockchain:
 * Fleksibilitas Pendekatan Pengembangan di Solana: Terdapat dua metode utama dalam membangun smart contract di jaringan Solana. Pengembangan menggunakan Native Rust menuntut penguasaan tingkat rendah terkait manajemen akun dan entrypoint program, yang sangat baik untuk memahami fundamental arsitektur Solana. Di sisi lain, penggunaan Anchor Framework terbukti menawarkan efisiensi dan kecepatan pengembangan yang jauh lebih tinggi berkat adanya makro abstraksi dan struktur proyek yang terstandardisasi.

 * Pentingnya Siklus Pengujian Terisolasi: Proses deployment ke jaringan utama (Mainnet) yang bersifat permanen (immutable) membuat fase pengujian menjadi sangat krusial. Penggunaan library seperti litesvm sangat efektif untuk melakukan simulasi dan unit testing secara cepat di lingkungan lokal. Selanjutnya, pemanfaatan validator lokal (localhost) dan jaringan uji publik (Devnet) mematangkan kesiapan program sebelum benar-benar di-deploy.

 * Universalitas Konsep Desentralisasi: Melalui tugas eksplorasi pada ekosistem Layer 1 alternatif (Sui Blockchain), terbukti bahwa konsep dasar pengembangan smart contract bersifat universal. Meskipun terdapat perbedaan radikal pada sintaksis bahasa (Rust vs. Sui Move) dan arsitektur basis datanya, siklus hidup pengembangan tetap konsisten: penulisan logika, kompilasi ke bytecode, pengujian, dan publikasi (deployment) menggunakan otorisasi dompet digital.

 * Relevansi Kompetensi: Secara keseluruhan, praktikum ini berhasil menguatkan kompetensi teknis dasar di bidang Informatika, khususnya dalam rekayasa perangkat lunak terdesentralisasi (Web3). Pemahaman alur kerja kompilasi dan deployment ini menjadi fondasi yang kokoh untuk membangun aplikasi terdesentralisasi (dApps) berskala besar.

