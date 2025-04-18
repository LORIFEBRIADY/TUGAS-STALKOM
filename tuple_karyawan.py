print("====================================================")
print("===========DAFTAR NAMA KARYAWAN PT. SIS II===========")
print("====================================================")

d_user = {"ptsis2": "ptsis2"}  

def login():
    username = input("Masukkan Username anda : ")
    if username not in d_user:
        print("Username salah. Silakan coba lagi.")
        return False

    password = input("Masukkan Password anda: ")
    if password != d_user[username] :
        print("Password salah. Silakan coba lagi.")
        return False
    return True

if login():
    karyawan = []
    while True:
        data_karyawan = input("Masukkan data karyawan (nama,jabatan,gaji) dipisahkan koma (atau ketik '0'): ")
        if data_karyawan.lower() == '0' :
            break
        try:
            nama, jabatan, gaji = data_karyawan.split(',')
            gaji = int(gaji.strip())
            if gaji <= 0:
                raise ValueError("Gaji harus lebih besar dari 0")
            karyawan.append((nama.strip(), jabatan.strip(), gaji))
        except ValueError as e:
            print(f"Format input salah. {e} Gunakan format 'nama,jabatan,gaji'. Pastikan gaji berupa angka. Silakan coba lagi.")

    def tampilkan_daftar(data_karyawan):
        if data_karyawan:
            print("\nDAFTAR NAMA KARYAWAN PT. SIS II : ")
            for i, item in enumerate(data_karyawan, 1):
                nama, jabatan, gaji = item
                print(f"{i}. Nama: {nama}, Jabatan: {jabatan}, Gaji: Rp. {gaji}")
        else:
            print("\nSilakan isi data karyawan dulu.")

    tampilkan_daftar(karyawan)
else:
    print("Akses ditolak.")


print("====================================================")
print("=============""Melayani dengan sepenuh hati""=============")
print("====================================================")
