print("=====================================================")
print("=========WELCOME TO KAMUS ISTILAH DI KAMPUS=========")
print("=====================================================")

kamuskampus = {
    "maba" : "mahasiswa baru",
    "sks" : "satuan kredit semester yaitu bobot pendidikan tiap mata kuliah",
    "ktm" : "kkartu tanda mahasiswa yagn wajib dimiliki oelh setiap mahasisiwa",
    "krs" : "kartu rencana studi yang harus diisi sebelum mulainya semester",
    "matkul" : "mata kuliah yaitu pelajaran yang diambil dalam pengisian krs dan dipelajari selama semester",
    "ip" : "indeks prestasi yaitu nilai akhir semester",
    "ipk" : "indeks prestasi komulatif yaitu rata rata nilai ip",
    "ukm" : "unit kegiatan kampus yaitu ekstra kulikuler kegiatan di kampus",
    "pkl" : "praktik kerja lapangan adalah mahasiswa yang magang kerja di kantor",
    "kkn" : "kuliah kerja nyata adalah mahasiswa yang mengabdikan diri ke masyarakat",
    "bem" : "badan eksekutif mahasiswa, osisnya kampus",
    "khs" : "kartu hasil studi yagn memuat hasil nilai selama perkuliahan",
    "prodii" : "program study",
    "spp" : "sumbangan pembinaan pendidikan",
    "pa" : "Pembi,bing akademik"
}

def cari_arti(kata):
    kata = kata.lower()
    if kata in kamuskampus:
        return kamuskampus[kata]
    else:
        return "Maaf, ini bukan istilah kampus."

while True:
    kata = input("Masukkan kata (atau ketik 'k' untuk berhenti) : ")
    if kata.lower() == "k":
        break
    arti = cari_arti(kata)
    print(f"Arti '{kata}': {arti}")
    
print("=================================================================")
print("=========TERIMA KASIH SUDAH MENGGUNAKAN KAMUS KAMPUS=========")
print("=================================================================")
