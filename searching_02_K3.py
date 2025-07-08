def linear_search(data, target):
    keys = list(data.keys())
    for x in range(len(keys)):
        if keys[x] == target:
            return x
    return -1

data = {
    "SI21240002": {
        "1. Nama"            : "ASTI ANANTA",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "21 Tahun",
        "5. Alamat"           : "Kopang"
    },
    "SI21240004": {
        "1. Nama"            : "BAIQ SALVANEZA ZULAEKA",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "18 Tahun",
        "5. Alamat"           : "Ketara"
    },
    "SI21240041": {
        "1. Nama"            : "INDAH NURHAYATI",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "22 Tahun",
        "5. Alamat"           : "Praya"
    },
    "SI21240017": {
        "1. Nama"            : "NAUFATUL AZZURA",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "18 Tahun",
        "5. Alamat"           : "Leneng"
    },
    "SI21240013": {
        "1. Nama"            : "LORI FEBRIADY",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "45 Tahun",
        "5. Alamat"           : "Praya"
    },
    "SI21240001": {
        "1. Nama"            : "DAMAN HURI",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "22 Tahun",
        "5. Alamat"           : "Batukliang"
    },
    "SI21240003": {
        "1. Nama"            : "BAIQ ASNA AQILAH",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "20 Tahun",
        "5. Alamat"           : "Praya"
    },
    "SI21240005": {
        "1. Nama"            : "FATMAH",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "19 Tahun",
        "5. Alamat"           : "Darmaji"
    },
    "SI21240006": {
        "1. Nama"            : "HISNUL PRADANA",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "19 Tahun",
        "5. Alamat"           : "Praya"
    },
    "SI21240010": {
        "1. Nama"            : "LALU NAZARUL IMAM",
        "2. Jurusan"         : "Sistem Informasi",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "21 Tahun",
        "5. Alamat"           : "Durian"
    },
    "TI21240001": {
        "1. Nama"            : "AHMAD IHZAT",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "19 Tahun",
        "5. Alamat"           : "Durian"
    },
    "TI21240002": {
        "1. Nama"            : "ALFAT ARYA ADI CANDRA",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "19 Tahun",
        "5. Alamat"           : "Durian"
    },
    "TI21240006": {
        "1. Nama"            : "FAHRURROZY",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Laki-Laki",
        "4. Usia"               : "20 Tahun",
        "5. Alamat"           : "Bonjeruk"
    },
    "TI21240011": {
        "1. Nama"            : "Linda Ayu Safitri",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin"   : "Perempuan",
        "4. Usia"            : "20 Tahun",
        "5. Alamat"          : "Janapria"
    },
    "TI21240014": {
        "1. Nama"            : "mardiana sari",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "20 Tahun",
        "5. Alamat"           : "Barebali"
    },
    "TI21240017": {
        "1. Nama"            : "NURUL HASANAH FEBRIANI",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"              : "19 Tahun",
        "5. Alamat"          : "Praya"
    },
    "TI21240022": {
        "1. Nama"            : "WINA HAYATI",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "19 Tahun",
        "5. Alamat"           : "Darmaji"
    },
    "TI21240028": {
        "1. Nama"            : "ZULFA ISMI ZURAIDA",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "20 Tahun",
        "5. Alamat"           : "Batujai"
    },
    "TI21240005": {
        "1. Nama"            : "BAIQ AGESTIA CAHYA ILAMI",
        "2. Jurusan"         : "Teknik Informatika",
        "3. Jenis kelamin": "Perempuan",
        "4. Usia"               : "20 Tahun",
        "5. Alamat"           : "PENGADANG"
    }
}

print("        WELCOME TO PROGRAM ALGORITMA ")
print("SEARCING DATA MAHASISWA BERDASARKAN NIM")
print()
target = input("Masukkan NIM: ")
index = linear_search(data, target)
print()

if index != -1:
    print(f"NIM {target} ditemukan di indeks ke {index}")
    print()
    print(f"Data Mahasiswa dengan NIM {target} sebagai berikut:")
    print("========================================")
    print(f"1. Nama              : {data[target]['1. Nama']}")
    print(f"2. Jurusan           : {data[target]['2. Jurusan']}")
    print(f"3. Jenis Kelamin : {data[target]['3. Jenis kelamin']}")
    print(f"4. Usia                : {data[target]['4. Usia']}")
    print(f"5. Alamat            : {data[target]['5. Alamat']}")
    print("========================================")
else:
    print(f"Nim {target} tidak ditemukan")
