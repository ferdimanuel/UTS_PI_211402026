from datetime import datetime, timedelta

def main():
    # Masukkan jumlah hari 
    num_days = int(input("Masukkan jumlah hari : "))

    # Mengambil tanggal sekarang
    tanggal_sekarang = datetime.now()

    # Hitung tanggal setelah ditambah
    tanggal_mendatang = tanggal_sekarang + timedelta(days=num_days)

    # Format tanggal di masa depan sesuai soal
    format_tanggal = tanggal_mendatang.strftime("%A, %d %B %Y")

    # Cetak tanggal yang diformat
    print("Tanggal", num_days, "hari dari sekarang adalah:", format_tanggal)

if __name__ == "__main__":
    main()
