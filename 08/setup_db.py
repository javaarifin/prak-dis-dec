from sqlmodel import Field, Session, SQLModel, create_engine

# 1. Tentukan Struktur Tabel Barang
class Barang(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True) # Tipe data INT
    kode_barang: str = Field(max_length=5)                 # Tipe data CHAR(5)
    nama_barang: str = Field(max_length=50)                # Tipe data VARCHAR(50)
    is_ready: bool                                         # Tipe data BOOLEAN
    harga: float                                           # Tipe data FLOAT

# 2. Buat file database SQLite baru bernama inventaris.db
engine = create_engine("sqlite:///inventaris.db")

# Fungsi untuk membuat tabel berdasarkan struktur di atas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# 3. Buat fungsi untuk memasukkan 5 data contoh ke database
def insert_data():
    barang1 = Barang(kode_barang="B0001", nama_barang="Buku Tulis", is_ready=True, harga=5000.0)
    barang2 = Barang(kode_barang="B0002", nama_barang="Pena Hitam", is_ready=True, harga=3000.0)
    barang3 = Barang(kode_barang="B0003", nama_barang="Pensil 2B", is_ready=False, harga=2500.0)
    barang4 = Barang(kode_barang="B0004", nama_barang="Penggaris 30cm", is_ready=True, harga=4000.0)
    barang5 = Barang(kode_barang="B0005", nama_barang="Penghapus Karet", is_ready=False, harga=1500.0)

    # Simpan data ke dalam database
    with Session(engine) as session:
        session.add_all([barang1, barang2, barang3, barang4, barang5])
        session.commit()

# Perintah untuk menjalankan fungsi di atas saat file ini dieksekusi
if __name__ == "__main__":
    create_db_and_tables()
    insert_data()
    print("Sukses! Database inventaris.db dan 5 data barang berhasil dibuat.")