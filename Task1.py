import datetime
import math

def main():
    # Mendapatkan jumlah hari 
    tahun_sekarang = datetime.datetime.now().year
    jumlah_hari = 366 if kabisat(tahun_sekarang) else 365

    # Membaca input 
    angka = int(input("Masukkan sebuah angka: "))

    # Melakukan pembagian
    hasil = angka / jumlah_hari

    # Pembulatan ke desimal 
    hasil_akhir = math.ceil(hasil * (10 ** 11)) / (10 ** 11)

    # Menampilkan output
    print("Hasil:", hasil_akhir)

    # Fungsi pengecekan tahun kabisat
def kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
if __name__ == "__main__":
    main()
