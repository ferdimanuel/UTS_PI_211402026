class BMI:
    def __init__(diri, berat, tinggi):
        diri.berat = berat
        diri.tinggi = tinggi
    
    @property
    def berat(diri):
        return diri._berat
    
    @berat.setter
    def berat(diri, nilai):
        if nilai <= 0:
            raise ValueError("Berat harus lebih besar dari nol (dalam pound).")
        diri._berat = nilai
    
    @property
    def tinggi(diri):
        return diri._tinggi
    
    @tinggi.setter
    def tinggi(diri, nilai):
        if nilai <= 0:
            raise ValueError("Tinggi harus lebih besar dari nol (dalam feet).")
        diri._tinggi = nilai
    
    def BMI_Value(diri):
        return (diri.berat / (diri.tinggi ** 2))  

    def __eq__(diri, lainnya):
        return diri.berat == lainnya.berat and diri.tinggi == lainnya.tinggi


# Membuat dua objek BMI
bmi1 = BMI(200, 8)
bmi2 = BMI(150, 5.6)

# Menghitung dan mencetak nilai BMI
print("BMI untuk orang - 1 :", bmi1.BMI_Value())
print("BMI untuk orang - 2:", bmi2.BMI_Value())

# Membandingkan dua objek BMI
if bmi1 == bmi2:
    print("Orang pertama dan orang kedua memiliki BMI yang sama.")
else:
    print("Orang pertama dan orang kedua memiliki BMI yang berbeda.")
