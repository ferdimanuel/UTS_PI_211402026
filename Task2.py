import datetime

def main():
    # Ambil tanggal hari ini
    tanggal_hari = datetime.date.today()

    # Ambil nilai hari dari tanggal hari ini
    tanggal_ujian = tanggal_hari.day

    # Hitung hasil faktorial dari tanggal hari ini
    hasil = faktorial(tanggal_ujian)

    # Print output
    print("Hasil faktorial dari tanggal ujian (", tanggal_hari, ") adalah:", hasil)

    # Fungsi untuk menghitung faktorial
def faktorial(n):
    # Jika angka yang dimasukkan adalah 0, maka hasilnya adalah 1
    if n == 0:  
        return 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
        return hasil

if __name__ == "__main__":
    main()
