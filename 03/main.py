# Mengimpor class VectorClock dari modul VectorClock.py
from VectorClock import VectorClock

print("=== Simulasi Penggunaan Modul Vector Clock ===")

# Menginisialisasi sistem dengan 2 proses (P0 dan P1)
p0 = VectorClock(num_processes=2, process_id=0)
p1 = VectorClock(num_processes=2, process_id=1)

print("\n[Kondisi Awal]")
print(p0)
print(p1)

print("\n[Event 1: P0 melakukan tugas internal]")
p0.increment()
print(p0)

print("\n[Event 2: P0 mengirim pesan ke P1]")
pesan_dari_p0 = p0.send_message()
p1.receive_message(pesan_dari_p0)

print("Status Vektor Saat Ini:")
print(p0)
print(p1)

print("\n[Pengecekan Kausalitas]")
cek_happens_before = p0.happens_before(p1)
print(f"Apakah Event di P0 terjadi sebelum Event di P1? : {cek_happens_before}")