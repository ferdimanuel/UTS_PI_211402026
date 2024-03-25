def main():
    # Membaca angka dari file input
    with open("input.txt", "r") as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    # Menghitung jumlah dari file innput
    total = sum(numbers)

    # Mencetak output dengan desimal
    print("{:,.3f}".format(total))

if __name__ == "__main__":
    main()
