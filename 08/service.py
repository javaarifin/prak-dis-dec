from typing import List
from fastapi import Depends, FastAPI
from sqlmodel import Session, select, create_engine
from setup_db import Barang  # Mengambil struktur tabel Barang dari file setup_db.py

# Koneksikan program ini ke file database yang sudah kita buat tadi
engine = create_engine("sqlite:///inventaris.db")

# Fungsi pembantu untuk membuka dan menutup koneksi database secara otomatis
def get_session():
    with Session(engine) as session:
        yield session

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Membuat RESTful API endpoint di alamat URL: /barang/
@app.get("/barang/", response_model=List[Barang])
def read_barang(session: Session = Depends(get_session)):
    # Perintah SQL untuk mengambil semua data dari tabel Barang
    statement = select(Barang)
    results = session.exec(statement).all()
    return results