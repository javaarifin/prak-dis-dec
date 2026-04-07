class VectorClock:
    def __init__(self, num_processes, process_id):
        self.clocks = [0] * num_processes  # Menginisialisasi semua jam ke angka nol
        self.process_id = process_id       # ID dari proses saat ini

    def increment(self):
        """Menambahkan +1 pada jam lokal untuk proses saat ini."""
        self.clocks[self.process_id] += 1

    def send_message(self):
        """Menyiapkan vector clock untuk dikirim bersama pesan."""
        self.increment()  # Tambah +1 jam lokal sebelum mengirim
        return list(self.clocks)  # Kembalikan salinan vector clock saat ini

    def receive_message(self, received_clocks):
        """Memperbarui vector clock saat menerima pesan."""
        for i in range(len(self.clocks)):
            self.clocks[i] = max(self.clocks[i], received_clocks[i])
        self.increment()  # Tambah +1 jam lokal setelah menerima dan menggabungkan

    def __str__(self):
        return f"P{self.process_id}: {self.clocks}"

    def happens_before(self, other_vector_clock):
        """
        Menentukan apakah vector clock ini terjadi sebelum yang lain.
        A happens before B jika semua elemen di A <= elemen di B, 
        dan minimal ada satu elemen di A yang < elemen di B.
        """
        if self.clocks == other_vector_clock.clocks:
            return False  # Jam sama, bukan 'happens before'

        all_le = True  # Semua elemen kurang dari atau sama dengan
        any_lt = False # Minimal ada satu elemen yang kurang dari

        for i in range(len(self.clocks)):
            if self.clocks[i] > other_vector_clock.clocks[i]:
                return False  # Bukan 'happens before' jika ada elemen yang lebih besar
            if self.clocks[i] < other_vector_clock.clocks[i]:
                any_lt = True

        return all_le and any_lt

    def is_concurrent(self, other_vector_clock):
        """
        Menentukan apakah dua vector clock terjadi bersamaan (concurrent).
        Dua event disebut concurrent jika tidak ada yang terjadi sebelum yang lain.
        """
        return not (self.happens_before(other_vector_clock) or
                    other_vector_clock.happens_before(self))