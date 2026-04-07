# LAPORAN PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI #

---
## Minggu 2

------
Nama    : Muhammad Java Arifin

NIM     : 235410073

-----
 ## Sinkronisasi pada Sistem Terdistribusi

 ### I Sinkronisasi Waktu
 1. Menginstall Net Time di windows dengan link berikut : https://www.timesynctool.com/
 
 2. setelah install Net Time lalu buka aplikasi Network Time lalu amati proses sinkronisasi

    ![](Images/Proses%20Net%20Time.png)


    Gambar diatas merupakan proses sinkronisasi beriikut rician proses sinkronisasi
    
    - Server yang digunakan nettime.pool.ntp.org dengan status koneksi (Good) yang berarti baik

    -   Waktu eksekusi atau Last Sync berhasil di eksekusi pada pukul 08:42:23

    - Offset di time komputer saya lambat 2,438 detik  dan jeda jaringan saat mengambil data lag 26ms
    
    - Next Attempt: Aplikasi ini bekerja otomatis di latar belakang (Mode: Windows Service). Untuk menjaga presisi jam secara berkala, sistem sudah menjadwalkan proses sinkronisasi berikutnya yang akan otomatis berjalan dalam 11 jam 36 menit 14 detik lagi.

### II Vector Clock
Vector clock digunakan untuk pengurutan event dalam suatu sistem terdistribusi. Berikut
adalah contoh source code untuk vector clock (ada pada source code: vclocks.py). Source
code diambil dari banyak sumber di Internet

    class VectorClock:
        def __init__(self, num_processes, process_id):
            self.clocks = [0] * num_processes  # Initialize all clocks to zero
            # The ID of the current process
            self.process_id = process_id

        def increment(self):
            """Increments the local clock for the current process."""
            self.clocks[self.process_id] += 1

        def send_message(self):
            """Prepares the vector clock for sending with a message."""
            self.increment()  # Increment local clock before sending
            return list(self.clocks)  # Return a copy of the current vector clock

        def receive_message(self, received_clocks):
            """Updates the vector clock upon receiving a message."""
            for i in range(len(self.clocks)):
                self.clocks[i] = max(self.clocks[i], received_clocks[i])
            self.increment()  # Increment local clock after receiving and merging

        def __str__(self):
            return f"P{self.process_id}: {self.clocks}"

        def happens_before(self, other_vector_clock):
            """
            Determines if this vector clock happens before another.
            A happens before B if all elements in A are less than or equal to
            the corresponding elements in B, and at least one element in A is
            strictly less than the corresponding element in B.
            """
            if self.clocks == other_vector_clock.clocks:
                return False  # Same clocks, not "happens before"

            all_le = True  # All elements are less than or equal
            any_lt = False  # At least one element is strictly less than

            for i in range(len(self.clocks)):
                if self.clocks[i] > other_vector_clock.clocks[i]:
                    return False  # Not "happens before" if any element is greater
                if self.clocks[i] < other_vector_clock.clocks[i]:
                    any_lt = True

            return all_le and any_lt

        def is_concurrent(self, other_vector_clock):
            """
            Determines if two vector clocks are concurrent.
            Two events are concurrent if neither happens before the other.
            """
            return not (self.happens_before(other_vector_clock) or
                        other_vector_clock.happens_before(self))


    # Simulate a system with 3 processes
    vc0 = VectorClock(num_processes=3, process_id=0)
    vc1 = VectorClock(num_processes=3, process_id=1)
    vc2 = VectorClock(num_processes=3, process_id=2)

    print(vc0)
    print(vc1)
    print(vc2)

    # Process 0 performs a local event
    vc0.increment()
    print(vc0)

    # Process 0 sends a message to Process 1
    message_from_p0 = vc0.send_message()
    vc1.receive_message(message_from_p0)
    print(vc0)
    print(vc1)

    # Process 2 performs a local event
    vc2.increment()
    print(vc2)

    # Process 1 sends a message to Process 2
    message_from_p1 = vc1.send_message()
    vc2.receive_message(message_from_p1)
    print(vc1)
    print(vc2)

    # Check causality
    print(f"vc0 happens before vc1: {vc0.happens_before(vc1)}")
    print(f"vc1 happens before vc0: {vc1.happens_before(vc0)}")
    print(f"vc0 is concurrent with vc2: {vc0.is_concurrent(vc2)}")

### Tugas
1. Jalankan program tersebut, amati keluarannya. Buat penjelasan dari keluaran
tersebut: bandingkan dengan algoritma tersebut jika vector clocks dilaksanakan
secara manual.

    setelah saya amati keluarannya program diatas berikut penjelasan saya :

    - Event Lokal: Setiap ada kejadian, proses hanya menambah nilai +1 pada indeksnya sendiri. (Contoh: P0 berubah dari [0, 0, 0] menjadi [1, 0, 0]).

    - Terima Pesan: Saat menerima pesan, sistem mengambil nilai tertinggi (max) dari setiap elemen antara vektor miliknya sendiri dan vektor dari pesan tersebut. Setelah itu, sistem menambah +1 pada indeksnya sendiri. (Contoh: P2 [0, 0, 1] menerima pesan P1 [2, 2, 0], nilai gabungan tertingginya [2, 2, 1], lalu indeks P2 ditambah 1 sehingga hasil akhirnya [2, 2, 2]).

    - Uji Kausalitas: Status happens_before terbukti True jika semua angka pada vektor pertama lebih kecil atau sama dengan vektor kedua. Dua kejadian dianggap concurrent (berjalan bersamaan) jika tidak ada yang saling mendahului. Karena vc0 mendahului vc1, dan vc1 mendahului vc2, maka vc0 tidak concurrent dengan vc2 (bernilai False).



2. Buat modul Python untuk class VectorClock tersebut dan buatlah contoh cara
menggunakan modul tersebut.